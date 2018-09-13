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
from jenkins_common import JenkinsJob


class DataInterface(object):
    '''
    A interface for communicating data between Jenkins and backends (e.g.: database)
    Jenkins will call these method, and a backend should implete the interface.
    '''
    @abstractmethod
    def require_data(self, type=None, **kwargs):
        '''
        params:
             type: data type, a concrete monitor task use this type to require data
        '''
        raise NotImplementedError

    @abstractmethod
    def publish_result(self, data, **kwargs):
        raise NotImplementedError


class JenkinsMonitorTbl(object):
    '''
    Jenkins monitor table
    items format: ((url_1, user_1, passwd_1, job_1), (url_2, user_2, passwd_2, job_2),)
    '''

    def __init__(self, task_name=None):
        self.db = Pymysql()

        # ((jenkins_id, jobs_id),)
        self.monitor_task = self._retrieve_data(task_name)

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
    def items(self):
        return self.monitor_task


class JenkinsMonitorTask(object):
    '''
    A common task for Jenkins jobs monitoring
    A concrete task should inherit the task and implete the process method
    Attributes:
        url: Jenkins URL, such as 'http://1.1.1.1:8080"
        user: Jenkins user
        passwd: Jenkins password
        impl: A bcakend, which should implete the methods of DataInterface
    '''

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
    '''
    A manager for jenkins jobs monitoring, it brings all monitoring tasks up.
    It takes a simple thread mode, each task was ran on a thread, the manager 
    will wait until all threads get done. If there are a lot of tasks, it's better 
    using thread pool mode instead this mode.
    '''

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
