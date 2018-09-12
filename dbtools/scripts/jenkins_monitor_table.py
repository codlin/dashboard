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


class JenkinsMonitorTbl(object):
    def __init__(self):
        self.db = Pymysql()

        self.jenkins_tuples = ()
        self.jenkins_dict = dict()

        self.monitor_jobs = dict()
        self.jenkins_monitor = []

        self._retrieve_data()

        self.db.close_DB()

    def _retrieve_data(self):
        self._retrieve_jenkins_info()
        self._retrieve_monitor_job()
        self._retrieve_jenkins_monitor()

    def _retrieve_jenkins_info(self):
        sql = r"select * from crt_jenkins_info"
        results = self.db.get_DB(sql)
        print(results)
        self.jenkins_tuples = results

        for item in results:
            self.jenkins_dict[item.id] = item
            self.jenkins_dict[item.url] = item.id

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
    def jenkins_tuples(self):
        return self.jenkins_tuples

    @property
    def jenkins_dict(self):
        return self.jenkins_dict

    @property
    def monitor_jobs(self):
        return self.monitor_jobs

    @property
    def jenkins_monitor(self):
        return self.jenkins_monitor

    def get_jekins_job_ids(self, jenkins_url, job_name):
        pass


if __name__ == '__main__':
    # test loadTestlinesTblCUID
    pass
