#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=E0401
import os
import sys

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, root)
from scripts.load_summary import main


def task_entry():
    print('load_status task is starting...')
    main()
    print('load_status task is done.')
