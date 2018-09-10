# pylint: disable=E0401
import os
import sys

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, root)
from scripts import *


def task_entry():
    print('task is running...')
