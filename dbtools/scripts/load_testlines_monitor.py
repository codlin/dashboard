#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from datetime import datetime
import pymysql
import csv
import codecs
import time

from MYSQL import Pymysql
from jenkins_monitor import JenkinsMonitorTask, DataInterface

# require data type
UNFINISHED_BUILD_ID = 'UNFINISHED_BUILD_ID'
LATEST_BUILD_ID = 'LATEST_BUILD_ID'


class FilteredBuildInfo(object):
    def __init__(self):
        self.buid_id = ""
        self.build_status = ""
        self.build_time = ""
        self.build_url = ""


def parse_build_data(build):
    json_data = build.json_data
    info = FilteredBuildInfo()
    info.loadname = ""
    info.testline = ""
    info.btsid = ""

    params = build.get_params()
    for param in params:
        if 'load' in param['name']:
            info.loadname = param['value']
        elif 'sites' in param['name']:
            info.testline = param['value']
        elif 'btsid' in param['name']:
            info.btsid = param['value']

    if info.loadname == "":
        display_name = json_data['displayName']
        info.loadname = display_name[-1:29]

    info.buid_id = json_data['id']
    info.build_status = json_data['result']
    info.build_time = build.timestamp
    info.build_url = build.console_url

    return info


class JenkinsJobBuildMonitorTask(JenkinsMonitorTask):
    def __init__(self, **kwargs):
        super(JenkinsJobBuildMonitorTask, self).__init__(**kwargs)

    # data should be builds id in array
    def process(self):
        data = []
        builds = self.impl.require_data(
            UNFINISHED_BUILD_ID, url=self.url, job=self.job_name)
        for build_id in builds:
            build = self.jenkins.get_build(build_id)
            info = parse_build_data(build)
            data.append(info)

        db_last_build_id = self.impl.require_data(
            LATEST_BUILD_ID, url=self.url, job=self.job_name)
        last_build_id = self.jenkins.get_first_buildnumber()
        build_id = int(db_last_build_id)
        while build_id < int(last_build_id):
            build_id += 1
            build = self.jenkins.get_build(build_id)
            info = parse_build_data(build)
            data.append(info)

        print(data)
        return data

# databse operation


class loadTestlinesTblCUID(DataInterface):
    def __init__(self):
        self.db = Pymysql()

    def __del__(self):
        self.db.close_DB()

    def require_data(self, type, **kwargs):
        if type == UNFINISHED_BUILD_ID:
            return self.unfinished_buildid
        elif type == LATEST_BUILD_ID:
            url = kwargs['url']
            job = kwargs['job']
            return self.latest_buildid(url, job)
        else:
            print("Unsupport the type {}".format(type))

    def publish_result(self, data, url, job):
        for item in data:
            if not isinstance(item, FilteredBuildInfo):
                print("Unsupport date item {}.".format(item))
                continue

            if self._count_item(url, job, item.build_id):
                self._insert_item(url, job, item)
            else:
                self._update_item(url, job, item)

    def _count_item(self, url, job, build_id):
        sql = "SELECT count(*) FROM crt_load_testline_status_page \
               WHERE url = '{}' AND = '{}' AND = '{}'".format(url, job, build_id)
        count = self.db.get_DB(sql)
        return count

    def _insert_item(self, url, job, item):
        sql = "INSERT INTO crt_load_testline_status_page(loadname, testline, btsid, url, job, build_id, build_status, build_time, build_url) \
               VALUES({},{},{},{},{},{},{},{},{})".format(item.loadname, item.testline, item.btsid, url, job,
                                                          item.build_id, item.build_status, item.build_time, item.build_url)
        print(sql)
        results = self.db.get_DB(sql)
        print(results)

    def _update_item(self, url, job, item):
        pass

    @property
    def unfinished_buildid(self):
        sql = r"select build_id from crt_load_testline_status_page where build_status is null  or build_status = 'null' or build_status = ''"
        print(sql)
        results = self.db.get_DB(sql)
        print(results)
        builds = []
        for build in results:
            builds.append(build[0])
        return builds

    def latest_buildid(self, url, job):
        build_id = self._get_job_builds_id(url, job)
        print(build_id)
        return None if not build_id else build_id[0]

    def _get_job_builds_id(self, url, job):
        sql = "SELECT build_id FROM crt_load_testline_status_page \
               WHERE url = '{}' AND job = '{}' ORDER BY build_id DESC".format(url, job)
        # print(sql)
        results = self.db.get_DB(sql)
        # print(results)
        return results


def create_load_testlines_monitor_task():
    pass


if __name__ == '__main__':
    # test loadTestlinesTblCUID
    load_testline = loadTestlinesTblCUID()
