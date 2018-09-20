#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import json
import requests
from datetime import datetime
import pymysql
import csv
import codecs
import time
import logging

from MYSQL import Pymysql
from jenkins_common import convertToDateTime
from jenkins_monitor import JenkinsMonitorManager, JenkinsMonitorTbl, JenkinsMonitorTask, DataInterface
# pylint: disable=E0401
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, root)
from common.logger import logger
# logger = logging.getLogger(__name__)

'''
Data type for DataInterface.require_data
'''
DB_UNFINISHED_BUILD_ID = 'DB_UNFINISHED_BUILD_ID'
DB_LATEST_BUILD_ID = 'DB_LATEST_BUILD_ID'


class FilteredBuildInfo(object):
    def __init__(self):
        self.loadname = ""
        self.testline = ""
        self.btsid = "NA"
        self.build_id = ""
        self.build_status = ""
        self.build_time = ""
        self.build_url = ""


def _parse_build_data(json_data, build_params=None):
    info = FilteredBuildInfo()

    if build_params:
        logger.debug(build_params)
        for key, value in build_params.items():
            if 'load' in key:
                info.loadname = value
                logger.debug("load name: {}".format(value))
            elif 'sites' in key or 'nodes' in key:
                info.testline = value.replace('"', '')
                logger.debug("testline: {}".format(value))
            elif 'btsid' in key:
                info.btsid = value
                logger.debug("btsid: {}".format(value))

    info.build_id = json_data['id']
    logger.debug("testline: {}".format(info.build_id))

    info.build_status = json_data['result']
    logger.debug("build_status: {}".format(info.build_status))

    info.build_time = convertToDateTime(json_data['timestamp'])
    logger.debug("build_time: {}".format(info.build_time))

    info.build_url = '{}console'.format(json_data['url'])
    logger.debug("build_url: {}".format(info.build_url))

    if info.loadname == "" or info.testline == "":
        display_name = json_data['displayName']
        logger.debug(display_name)
        items = display_name.split('_')
        if len(items) < 7:
            logger.error("Can't parse load name and testline, abandon this build {}, {}.".format(
                info.build_id, info.build_url))
            return None

        info.loadname = "_".join(items[-5:])
        logger.debug("load name: {}".format(info.loadname))

        info.testline = items[1].replace('"', '')
        logger.debug("testline: {}".format(info.testline))

    return info


def _parse_builds_data(json_items):
    filteredItems = []
    for json_data in json_items:
        info = _parse_build_data(json_data)
        if info is None:
            continue

        filteredItems.append(info)

    return filteredItems


class JenkinsJobBuildMonitorTask(JenkinsMonitorTask):
    '''
    A concrete job monitor for load testline
    '''

    def __init__(self, **kwargs):
        super(JenkinsJobBuildMonitorTask, self).__init__(**kwargs)

    # data should be builds id in array
    def process(self):
        data = []
        builds = self.impl.require_data(DB_UNFINISHED_BUILD_ID,
                                        url=self.url, job=self.job_name)
        logger.debug(builds)
        for build_id in builds:
            build = self.jenkins.get_build(build_id)
            info = _parse_build_data(build.json_data, build.inner.get_params())
            logger.debug(info)
            data.append(info)

        db_last_build_id = self.impl.require_data(DB_LATEST_BUILD_ID,
                                                  url=self.url, job=self.job_name)
        last_build_id = self.jenkins.get_last_buildnumber()
        logger.info("{}-{}: db_last_build_id {}, jenkins last_build_id {}.".format(self.url, self.job_name,
                                                                                   db_last_build_id,
                                                                                   last_build_id))
        if db_last_build_id is None:
            filters = ['id', 'result', 'displayName', 'timestamp', 'url']
            json_data = self.jenkins.get_all_builds(filters)
            return data + _parse_builds_data(json_data)

        build_id = int(db_last_build_id)
        while build_id < int(last_build_id):
            build_id += 1
            build = self.jenkins.get_build(build_id)
            info = _parse_build_data(build.json_data, build.inner.get_params())
            data.append(info)

        logger.debug(data)
        return data


class loadTestlinesTblCUID(DataInterface):
    '''
    A backend for JenkinsJobBuildMonitorTask, provide data to task and post result into database.
    '''

    def __init__(self):
        self.db = Pymysql()

    def require_data(self, type, **kwargs):
        if type == DB_UNFINISHED_BUILD_ID:
            return self.unfinished_buildid
        elif type == DB_LATEST_BUILD_ID:
            url = kwargs['url']
            job = kwargs['job']
            return self.latest_buildid(url, job)
        else:
            logger.error("Unsupport the type {}".format(type))

    def publish_result(self, data, url, job):
        for item in data:
            if not isinstance(item, FilteredBuildInfo):
                logger.error("Unsupport date item {}.".format(item))
                continue

            if self._count_item(url, job, item) > 0:
                self._update_item(url, job, item)
            else:
                self._insert_item(url, job, item)

    def _insert_item(self, url, job, item):
        sql = "INSERT INTO crt_load_testline_status_page(loadname, testline, btsid, url, job, build_id, build_status, build_time, build_url) \
               VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(item.loadname, item.testline, item.btsid, url, job,
                                                                            item.build_id, item.build_status, item.build_time, item.build_url)
        logger.debug(sql)
        self.db.update_DB(sql)

    def _update_item(self, url, job, item):
        sql = "UPDATE crt_load_testline_status_page set build_status='{}', build_time='{}' \
               WHERE loadname='{}' AND testline='{}' AND url='{}' AND job='{}' \
               AND build_id='{}'".format(item.build_status, item.build_time, item.loadname, item.testline, url, job, item.build_id)
        logger.debug(sql)
        self.db.update_DB(sql)

    def _count_item(self, url, job, item):
        sql = "SELECT COUNT(*) FROM crt_load_testline_status_page \
               WHERE loadname='{}' AND testline='{}' AND url='{}' \
               AND job='{}' AND build_id='{}'".format(item.loadname, item.testline, url, job, item.build_id)

        count = self.db.get_DB(sql)
        logger.debug(count)
        return count[0][0]

    @property
    def unfinished_buildid(self):
        sql = r"select build_id from crt_load_testline_status_page where build_status is null  or build_status = 'null' or build_status = ''"
        logger.debug(sql)
        results = self.db.get_DB(sql)
        logger.debug(results)
        builds = []
        for build in results:
            builds.append(build[0])
        return builds

    def latest_buildid(self, url, job):
        build_id = self._get_job_builds_id(url, job)
        logger.debug(build_id)
        return None if not build_id else build_id[0][0]

    def _get_job_builds_id(self, url, job):
        sql = "SELECT build_id FROM crt_load_testline_status_page \
               WHERE url = '{}' AND job = '{}' ORDER BY CAST(build_id as unsigned) DESC".format(url, job)
        logger.debug(sql)
        results = self.db.get_DB(sql)
        logger.debug(results)
        return results


def _create_load_testlines_tasks():
    tasks = []
    items = JenkinsMonitorTbl("LOAD_TESTLINE").items
    logger.debug(items)
    for (url, user, passwd, job_name) in items:
        task = JenkinsJobBuildMonitorTask(url=url, user=user, passwd=passwd,
                                          job_name=job_name, impl=loadTestlinesTblCUID())
        tasks.append(task)

    return tasks


def load_testlines_task_entry():
    '''
    A task entry which can be added into python scheduler.
    '''
    tasks = _create_load_testlines_tasks()
    monitor = JenkinsMonitorManager(tasks)
    monitor.run()


if __name__ == '__main__':
    # test loadTestlinesTblCUID
    load_testlines_task_entry()
    # task = JenkinsJobBuildMonitorTask(url='http://135.242.139.122:8085', user='scpadm', passwd='scpadm',
    #                                   job_name='check_site_state_FDD_AICT3', impl=loadTestlinesTblCUID())

    # task.run()
