#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, root)
from scripts.load_testlines_monitor import load_testlines_task_entry

config = {
    'interval': 5  # minutes
}


def task_entry():
    print('load_testlines task is starting...')
    load_testlines_task_entry()
    print('load_testlines task is done.')
