#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from datetime import datetime
import pymysql
import csv
import codecs
import time
import threading
from abc import abstractmethod

from MYSQL import Pymysql
from jenkins import JenkinsJob


class DataInterface(object):
    @abstractmethod
    def require_data(self, type=None, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def publish_result(self, data, **kwargs):
        raise NotImplementedError


class JenkinsMonitorTbl(object):
    def __init__(self, task_name=None):
        self.db = Pymysql()

        # ((jenkins_id, jobs_id),)
        self.monitor_task = self._retrieve_data(task_name)

        self.db.close_DB()

    def _retrieve_data(self, task_name):
        sql = "SELECT jenkins.url, jenkins.user, jenkins.passwd, job.job \
               FROM crt_jenkins_monitor AS m, crt_jenkins_info AS jenkins, crt_jenkins_job AS job \
               WHERE m.jenkins_id = jenkins.id AND m.job_id = job.id"
        if task_name:
            sql += r" and task = '{}'".format(task_name)
        # print(sql)
        monitor_task = self.db.get_DB(sql)
        # print(monitor_task)
        return monitor_task

    @property
    def task(self):
        return self.monitor_task


class JenkinsMonitorTask(object):
    def __init__(self, url, user, passwd, job_name, impl):
        self.url = url
        self.job_name = job_name
        self.jenkins = JenkinsJob(url, user, passwd, job_name)
        self.impl = impl

    @abstractmethod
    def process(self):
        raise NotImplementedError

    def run(self):
        result = self.process()
        ret = self.impl.publish_result(result, self.url, self.job_name)
        return ret


class JenkinsMonitorManager(object):
    def __init__(self, tasks):
        # init jenkins and jobs
        self.tasks = tasks
        self.thread_list = []

    def run(self):
        # for each task, start a thread
        for task in self.tasks:
            self.thread_list.append(threading.Thread(target=task.run))

        # start all sub-threads terminate
        for td in self.thread_list:
            td.start()

        # wait all sub-threads terminate
        for td in self.thread_list:
            td.join()


if __name__ == '__main__':
    pass
