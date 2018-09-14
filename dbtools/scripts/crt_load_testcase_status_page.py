#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ma xiaoquan
# @Contact: xiaoquan.ma@nokia-sbell.com
# @File: crt_load_testcase_status_page.py
# @Time: 2018/9/12 11:08
# @Desc:

import sys
import os
import pymysql
import pandas as pd
from datetime import datetime
from MYSQL import Pymysql
from function import *
import argparse
from pprint import pprint
import requests
import json
import urllib3

def parse_args():
    p = argparse.ArgumentParser(
        description='Request CRT data of project from mysql database',
        usage="%(prog)s [OPTION]... (type '-h' or '--help' for help)"
    )
    p.add_argument('-t', '--type', action='store', default='FLF', help="Get the project type of CRT")
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
    log.info('mode is: %s', mode)
    sql_str = '''
    select enb_build
    from test_results 
    where enb_build !='Null' and enb_build !='' and enb_build not like '%MF%' and crt_type='CRT1_DB' 
    and enb_release like("''' + crt_type + '''")
    GROUP BY enb_build 
    order by time_epoch_start desc limit 1
    '''
    data = mysqldb.get_DB(sql_str)
    results = []
    for row in data:
        loadname = row[0]
        results.append(loadname)
    return results


def get_release(loadname):
    branch = loadname.split('_')
    if branch[0]=="FLF17A" and branch[2]=='1000':
        result = "FLF17ASP"
    else:
        result = branch[0]
    return result


def get_testcase_total(loadname):
    barnch = get_release(loadname)
    logger.info('loadname branch is  %s' % get_release(loadname))
    sql_str = '''
        select count(*)
        from (select crt_testcase.casename
              from crt_testcase_release
                     INNER JOIN crt_testcase on crt_testcase_release.case_id = crt_testcase.id
              where crt_testcase_release.load_release = "''' + barnch + '''") as t
    '''
    data = mysqldb.get_DB(sql_str)
    result = data[0][0]
    return result


def get_load_name_time(loadname):
    sql_str = '''
    select FROM_UNIXTIME(min(time_epoch_start),'%Y-%m-%d %H:%i:%s') AS time 
    from test_results where enb_build="''' + loadname + '''" and crt_type='CRT1_DB' 
    '''
    data = mysqldb.get_DB(sql_str)
    result = data[0][0]
    return result


def get_passed_count(loadname):
    sql_str = '''
        select count(*)
        from (select test_case_name     
              from test_results
              where enb_build = "''' + loadname + '''"
                and crt_type = 'CRT1_DB'
                and record_valid = 1
                and test_status = 'passed'
              group by test_case_name) as t
    '''
    data = mysqldb.get_DB(sql_str)
    results = data[0][0]
    return results


def get_failed_count(loadname):
    sql_str = '''
        select count(*)
        from (select test_case_name
              from test_results
              where crt_type = 'CRT1_DB'
                and record_valid = 1
                and test_status != 'Passed'
                and enb_build = "''' + loadname + '''"
                and test_case_name not in(select test_case_name
                                          from test_results
                                          where enb_build = "''' + loadname + '''"
                                            and crt_type = 'CRT1_DB'
                                            and record_valid = 1
                                            and test_status = 'Passed'
                                          group by test_case_name)
              group by test_case_name
              order by robot_ip) as t;
    '''
    data = mysqldb.get_DB(sql_str)
    results = data[0][0]
    return results


def get_unexecuted_count(loadname):
    branch = get_release(loadname)
    logger.info('branch is %s', branch)
    sql_str = '''
        select count(*)
        from (select *
              from (select crt_testcase.casename
                    from crt_testcase_release
                           INNER JOIN crt_testcase on crt_testcase_release.case_id = crt_testcase.id
                    where crt_testcase_release.load_release = "''' + branch + '''") as crt_testcase
              where crt_testcase.casename not in
                    (SELECT test_case_name
                     from test_results
                     where enb_build = "''' + loadname + '''"
                       and record_valid = 1
                       and crt_type = 'CRT1_DB')) as t2
     '''
    data = mysqldb.get_DB(sql_str)
    results = data[0][0]
    return results


def get_passed_first_count(loadname):
    sql_str = '''
select count(*)
from (select enb_build,
             FROM_UNIXTIME(time_epoch_start, '%Y-%m-%d %h:%i:%s') AS time,
             test_line_id,
             robot_ip,
             test_case_name,
             test_status,
             enb_config
      from (select enb_build, time_epoch_start, test_line_id, robot_ip, test_case_name, test_status, enb_config
            from test_results
            where crt_type = 'CRT1_DB'
              and record_valid = 1
              and test_status = 'Passed'
              and enb_build = "''' + loadname + '''") t1
      where time_epoch_start < (select min(time_epoch_start) + '18000'
                                from (select enb_build,
                                             time_epoch_start,
                                             test_line_id,
                                             robot_ip,
                                             test_case_name,
                                             test_status,
                                             enb_config
                                      from test_results
                                      where crt_type = 'CRT1_DB'
                                        and record_valid = 1
                                        and test_status = 'Passed'
                                        and enb_build = "''' + loadname + '''") t2)
      group by test_case_name) as t3
    '''
    data = mysqldb.get_DB(sql_str)
    results = data[0][0]
    return results


def get_pass_rate(loadname, passed_count):
    testcase_total = get_testcase_total(loadname)
    logger.info('testcase_total: %s', testcase_total)
    result = round(passed_count / testcase_total * 100, 1)
    logger.info("pass_rate1: %s" % type(result))
    return result


def get_first_pass_rate(loadname, passed_count):
    testcase_total = get_testcase_total(loadname)
    logger.info('testcase_total: %s', testcase_total)
    result = round(passed_count / testcase_total * 100, 1)
    logger.info("pass_rate2: %s" % result)
    return result

def get_jenkins_data(url):
    response = requests.get(url, verify=False) # verify=False去掉鉴权
    data = response.text
    results = json.loads(data)
    return results

def get_debug_result(loadname):
    branch = loadname.split('_')
    if branch[0]=="FLF18A" and branch[2]=='9999':  #Trunk的包需要FLF18A替换成FLF00
        loadname = loadname.replace("FLF18A", "FLF00")
    logger.info('loadname is  %s :' ,loadname )
    a=get_jenkins_data('https://coop.int.net.nokia.com/ext/api/pci/build/buildinfo?buildid='+loadname+'')

    if branch[0]=="FLF17A" and branch[2]=='0000' or branch[0]=="FLF18": # FLF17A和FLF18 crt排第二个
        debug_status = a[0]['pci'][1]['children'][-1]['cases'][0]['result']
    else:
        debug_status = a[0]['pci'][0]['children'][-1]['cases'][0]['result']

    return debug_status

def main():
    crt_type = (parse_args().type)
    object = get_loadnames(crt_type)
    for name in object:
        logger.info("loadname is %s" % name)

        sql_str = '''
    select FROM_UNIXTIME(time_epoch_start,\"%Y-%m-%d %h:%i:%s\") AS time, 
    enb_build, test_case_name, test_line_id, robot_ip, test_status, test_suite
    from test_results 
    where crt_type='CRT1_DB' and record_valid=1  and test_status!='Passed' and enb_build="'''+name+ '''" and test_case_name 
    not in(
    select test_case_name from test_results where enb_build="'''+name+ '''"  and crt_type='CRT1_DB' and record_valid=1  
    and test_status='Passed' group by test_case_name ) group by test_case_name order by robot_ip 
                '''
        # logger.info('sql_str: %s', sql_str)
        data = mysqldb.get_DB(sql_str)
        item = data[0]
        pprint(data[0])


        # mysqldb.update_DB(sql_str)

if __name__ == "__main__":
    t_start = datetime.now()  # 起x始时间
    # urllib3.getproxies = lambda: {}  # 设置代理
    logger = set_log_level('INFO')
    logger.info('%s Start running %s' % ('-' * 10, '-' * 10))
    mysqldb = Pymysql()
    main()
    mysqldb.close_DB()
    t_end = datetime.now()  # 关闭时间
    time = (t_end - t_start).total_seconds()
    logger.info('The script run time is: %s sec' % (time))