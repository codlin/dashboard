import os
import sys


def get_files(path, suffix=''):
    if not os.path.exists(path):
        return None

    file_lst = list()
    get_dir_files(file_lst, path)
    if suffix == '':
        return file_lst

    files = list()
    for file in file_lst:
        _, ext = os.path.splitext(file)
        if suffix == ext:
            files.append(file)

    return files


def get_dir_files(file_list, path):
    files = os.listdir(path)
    for file in files:
        item = os.path.join(path, file)
        if os.path.isdir(item):
            get_dir_files(file_list, item)
        else:
            file_list.append(os.path.join(path, file))
