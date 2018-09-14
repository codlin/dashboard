import os
import sys
import imp
import time
from apscheduler.schedulers.background import BlockingScheduler
# pylint: disable=E0401
from common.helper import get_files
from common.logger import logger

root = os.path.join(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)


def load_tasks():
    tasks = list()
    path = os.path.join(root, 'tasks')
    files = get_files(path)
    i = 0
    for f in files:
        i += 1
        if f.endswith('__init__.py') or f.endswith('.pyc'):
            continue

        file_path = os.path.join(path, f)
        logger.info('load module from: {}'.format(file_path))
        item = imp.load_source('task_entry'+str(i), file_path)
        tasks.append(item)

    return tasks


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    tasks = load_tasks()
    for task in tasks:
        logger.info('add job: {}, interval[{}]'.format(
            task.config['name'], task.config['interval']))
        scheduler.add_job(task.task_entry, 'interval',
                          minutes=task.config['interval'])

    scheduler.start()
