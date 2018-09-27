#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ma xiaoquan
# @Contact: xiaoquan.ma@nokia-sbell.com
# @File: crt_testcase_status_page.py
# @Time: 2018/9/12 11:08
# @Desc:

import sys
import os
from datetime import datetime
import argparse
import urllib3
from pprint import pprint
import requests
import json
import pandas as pd
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, root)
from common.logger import logger, set_log_level
from scripts.mysql import Pymysql
mysqldb = Pymysql()


def parse_args():
    p = argparse.ArgumentParser(
        description='Request CRT data of project from mysql database',
        usage="%(prog)s [OPTION]... (type '-h' or '--help' for help)"
    )
    p.add_argument('-t', '--type', action='store', default='FLF',
                   help="Get the project type of CRT")
    args = p.parse_args()
    return args


def get_loadnames(mode):
    """
    :param type: FZM FDD = FLF
                 FZM TDD = TLF
                 CFZC FDD = FLC
                 CFZC TDD = TLC
    :return loadname list
    example: get_loadname('TLF')
    """
    crt_type = mode + '%'
    logger.debug('Type is: %s', mode)
    sql_str = '''
    select enb_build
    from test_results 
    where enb_build !='Null' and enb_build !='' and enb_build not like '%MF%' and crt_type='CRT1_DB' 
    and enb_release like("''' + crt_type + '''")
    GROUP BY enb_build 
    order by time_epoch_start desc limit 5
    '''
    data = mysqldb.get_DB(sql_str)
    results = []
    for row in data:
        loadname = row[0]
        results.append(loadname)
    return results


def get_release(loadname):
    branch = loadname.split('_')
    if branch[0] == "FLF17A" and branch[2] == '1000':
        result = "FLF17ASP"
    else:
        result = branch[0]
    return result


def get_load_name_time(loadname):
    sql_str = '''
    select FROM_UNIXTIME(min(time_epoch_start),'%Y-%m-%d %H:%i:%s') AS time 
    from test_results where enb_build="''' + loadname + '''" and crt_type='CRT1_DB' 
    '''
    data = mysqldb.get_DB(sql_str)
    result = data[0][0]
    return result


def get_failed(loadname):
    sql_str = '''
            select enb_build, test_case_name, test_line_id, robot_ip, test_status, test_suite
            from test_results
            where crt_type='CRT1_DB' and record_valid=1  and test_status!='Passed' and enb_build="''' + loadname + '''" and test_case_name
            not in(
            select test_case_name from test_results where enb_build="''' + loadname + '''"  and crt_type='CRT1_DB' and record_valid=1
            and test_status='Passed' group by test_case_name ) group by test_case_name order by robot_ip
    '''
    results = mysqldb.get_DB(sql_str)
    return results


def get_unexecuted(loadname):
    branch = get_release(loadname)
    logger.debug('branch is %s', branch)
    sql_str = '''
            SELECT *
            FROM (SELECT casename
                  FROM crt_testcase_name
                         INNER JOIN crt_testcase_release ON crt_testcase_release.case_id = crt_testcase_name.id
                  WHERE crt_testcase_release.load_release = "''' + branch + '''" 
                  GROUP BY casename) AS t1
            WHERE t1.casename NOT IN (SELECT test_case_name
                                      FROM test_results
                                      WHERE enb_build = "''' + loadname + '''" 
                                        AND record_valid = 1
                                        AND crt_type = 'CRT1_DB'
                                      GROUP BY test_case_name)
     '''
    results = mysqldb.get_DB(sql_str)
    return results


def list_to_str(list):
    str = ''
    for i in range(0, len(list)):
        item = '"' + list[i] + '",'
        str = str + item
    result = str[:-1]
    return result


def running(crt_type):
    t_start = datetime.now()  # 起x始时间
    # urllib3.getproxies = lambda: {}  # 设置代理
    logger.debug('%s Start running %s' % ('-' * 10, '-' * 10))
    object = get_loadnames(crt_type)
    for name in object:
        logger.debug("loadname is %s" % name)
        # 更新失败的用例
        data_failed = get_failed(name)

        # 更新未执行的用例
        data_unexecuted = get_unexecuted(name)

        # 循环输出failed的testcase，更新入数据库
        for i in range(0, len(data_failed)):
            item = data_failed[i]
            item = list(item)
            logger.debug('item is: %s', item)
            item = list_to_str(item)
            sql_str = '''
                REPLACE INTO crt_load_testcase_status_page(loadname,casename,btsid,node,result,suite) VALUES(''' + item + ''');
            '''
            logger.debug('sql_str: %s', sql_str)
            mysqldb.update_DB(sql_str)

        # 循环输出unexecuted的testcase，更新入数据库
        for i in range(0, len(data_unexecuted)):
            item = data_unexecuted[i]
            item = list(item)
            item = list_to_str(item)

            item = '"' + name + '"' + ',' + item + ',' + '"",' + '"",' + '"NULL"' + ',""'
            logger.debug('item is: %s', item)
            sql_str = '''
                REPLACE INTO crt_load_testcase_status_page(loadname,casename,btsid,node,result,suite) VALUES(''' + item + ''');
            '''
            logger.debug('sql_str: %s', sql_str)
            mysqldb.update_DB(sql_str)

    t_end = datetime.now()  # 关闭时间
    time = (t_end - t_start).total_seconds()
    logger.debug('The script run time is: %s sec' % (time))


def main():
    logger.info('load testcases status task began.')
    list_project = ['FLF', 'TLF', 'FLC', 'TLC']
    for i in range(len(list_project)):
        running(list_project[i])

    logger.info('load testcases status task done.')


if __name__ == "__main__":
    # crt_type = (parse_args().type)
    set_log_level("DBTools", 'DEBUG')
    main()
