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
from jenkins_monitor_table import JenkinsMonitorTbl

# databse operation


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

    def get_job_builds_id(self, jenkins_id, job_id):
        sql = r"select build_id from crt_load_testline_status_page where url_id = '{}' and job_id = '{}'".format(
            jenkins_id, job_id)
        # print(sql)
        results = self.db.get_DB(sql)
        # print(results)
        return results

    def get_unfinished_builds(self):
        sql = r"select * from crt_load_testline_status_page where build_status is null  or build_status = 'null' or build_status = ''"
        print(sql)
        results = self.db.get_DB(sql)
        print(results)
        return results

    def get_job_lastbuildid(self, jenkins_id, job_id):
        ids = self.get_job_builds_id(jenkins_id, job_id)
        return ids[0]


# jenkins operation
class JenkinsMonitor(object):
    def __init__(self):
        self.monitor = JenkinsMonitorTbl()
        self._init_jenkins()

    def _init_jenkins(self):
        jenkins = self.monitor.jenkins_tuples
        for jenkins_id, url, user, passwd in jenkins:
            monitor = JenkinsMonitor(url, user, passwd)
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
