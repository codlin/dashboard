import os
import sys
import imp

from apscheduler.schedulers.background import BackgroundScheduler
from helper import get_files

root = os.path.join(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)


def load_tasks():
    tasks = list()
    path = os.path.join(root, 'tasks')
    files = get_files(path)
    for f in files:
        if f == '__init__.py':
            continue

        file_path = os.path.join(path, f)
        item = imp.load_source('task_entry', file_path)
        tasks.append(item.task_entry)

    return tasks


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    tasks = load_tasks()
    for task_entry in tasks:
        scheduler.add_job(task_entry, 'interval', minute=5)

    scheduler.start()

    while True:
        pass
