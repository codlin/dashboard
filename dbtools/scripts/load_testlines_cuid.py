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
from jenkins import JenkinsMonitor


class JenkinsMonitorTbl(object):
    def __init__(self):
        self.db = Pymysql()
        self.jenkins_info = dict()
        self.monitor_jobs = dict()
        self.jenkins_monitor = []

        self._retrieve_data()

    def __del__(self):
        self.db.close_DB()

    def _retrieve_data(self):
        self._retrieve_jenkins_info()
        self._retrieve_monitor_job()
        self._retrieve_jenkins_monitor()

    def _retrieve_jenkins_info(self):
        sql = r"select * from crt_jenkins_info"
        results = self.db.get_DB(sql)
        print(results)
        for item in results:
            self.jenkins_info[item.id] = item
            self.jenkins_info[item.url] = item.id

    def _retrieve_monitor_job(self):
        sql = r"select * from crt_jenkins_job"
        results = self.db.get_DB(sql)
        print(results)
        for item in results:
            self.monitor_jobs[item.id] = item.job
            self.monitor_jobs[item.job] = item.id

    def _retrieve_jenkins_monitor(self):
        sql = r"select * from crt_jenkins_monitor"
        results = self.db.get_DB(sql)
        print(results)
        for item in results:
            self.jenkins_monitor.append(item)

    @property
    def jenkins_items(self):
        return self.jenkins_info

    @property
    def monitor_jobs(self):
        return self.monitor_jobs

    @property
    def jenkins_monitor(self):
        return self.jenkins_monitor


class loadTestlinesTblCUID(object):
    def __init__(self):
        self.db = Pymysql()

    def __del__(self):
        self.db.close_DB()

    def get_load_items(self, load_name):
        sql = r"select * from crt_load_testline_status_page where loadname = '{}'".format(
            load_name)
        results = self.db.get_DB(sql)
        return results

    def get_jenkins_items(self, jekins_url):
        jenkins_id = r"select id from crt_jenkins_info where url = '{}'".format(
            jekins_url)
        sql = r"select * from crt_load_testline_status_page where jenkins_id IN ({})".format(
            jenkins_id)
        # print(sql)
        results = self.db.get_DB(sql)
        # print(results)
        return results

    def get_unfinished_builds(self):
        sql = r"select * from crt_load_testline_status_page where upgrade_status is null  or upgrade_status = 'null'"
        print(sql)
        results = self.db.get_DB(sql)
        print(results)
        return results

    def get_checksite_lastbuildid(self, jenkins_id, job_id):
        jenkins_id = r"select id from crt_jenkins_info where url = '{}'".format(
            jekins_url)

        job = r"select id from crt_jenkins_job where url = '{}'".format(
            job_name)


class loadTestlinesJekins(object):
    def __init__(self):
        self.jenkins_monitor = []

        self._init_jenkins()

    def _init_jenkins(self):
        for jenkins in crt_jenkins:
            monitor = JenkinsMonitor(jenkins['url'], 'scpadm', 'scpadm')
            monitor.add_jobs(jenkins['jobs'])
            self.jenkins_monitor.append(monitor)

    def run(self):
        for monitor in self.jenkins_monitor:
            monitor
        pass


class loadTestlines(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    # test loadTestlinesTblCUID
    load_testline = loadTestlinesTblCUID()
    load_testline._retrieve_jenkins_monitor()
    load_testline.get_load_items('FLF18A_ENB_9999_180910_001006')
    load_testline.get_jenkins_items('http://10.52.200.190')
    load_testline.get_unfinished_builds()
