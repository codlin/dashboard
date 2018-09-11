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

fzmfdd_jobs = [
    'check_site_state_FDD_AICT3',
    'healthCheckup_AICT3_FDD',
    'upgrade_FDD_AICT3'
]

fzmtdd_jobs = [
    'check_site_state_TDD_AICT3',
    'healthCheckup_AICT3_TDD',
    'upgrade_TDD_AICT3'
]

fzc_jobs = [
    'check_site_state_cFZC_AICT',
    'upgrade_cFZC_AICT'
]

crt_jenkins = [
    {
        'url': 'http://10.52.200.190',
        'jobs': fzmfdd_jobs + fzmtdd_jobs
    },
    {
        'url': 'http://135.242.139.122:8085',
        'jobs': fzmfdd_jobs
    },
    {
        'url': 'http://135.242.139.122:8086',
        'jobs': fzmtdd_jobs
    },
    {
        'url': 'http://135.242.139.122:8087',
        'jobs': fzc_jobs
    },
    {
        'url': 'http://135.242.139.122:8088',
        'jobs': fzc_jobs
    }
]


class loadTestlinesTblCUID(object):
    def __init__(self):
        self.db = Pymysql()


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
    pass
