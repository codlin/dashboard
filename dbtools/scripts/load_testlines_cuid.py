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


class loadTestlines(object):
    def __init__(self):
        self.db = Pymysql()
        self.jenkins = JenkinsMonitor()


if __name__ == '__main__':
    pass
