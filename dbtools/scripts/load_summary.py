#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ma xiaoquan
# @Contact: xiaoquan.ma@nokia-sbell.com
# @File: load_summary.py
# @Time: 2018/9/6 11:08
# @Desc:

import sys
import os
import pymysql
from datetime import datetime
from MYSQL import Pymysql
from function import *
import argparse
from pprint import pprint
import pandas as pd


def parse_args():
    p = argparse.ArgumentParser(
        description='Request CRT data of project from mysql database',
        usage="%(prog)s [OPTION]... (type '-h' or '--help' for help)"
    )
    p.add_argument('-t', '--type',  action='store', default='FLF',help="Get the project type of CRT")
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
    log.debug('mode: %s', mode)
    sql_str = '''
    select enb_build
    from test_results 
    where enb_build !='Null' and enb_build !='' and enb_build not like '%MF%' and crt_type='CRT1_DB' 
    and enb_release like("''' + crt_type + '''")
    GROUP BY enb_build 
    order by time_epoch_start desc limit 20 
    '''
    results = mysqldb.get_DB(sql_str)
    loadnames=[]
    for row in results:
        loadname = row[0]
        loadnames.append(loadname)
    return loadnames

def get_load_name_time(loadname):
    sql_str='''
    select FROM_UNIXTIME(min(time_epoch_start),"%Y-%m-%d %H:%i:%s") AS time 
    from test_results where enb_build="''' + loadname + '''" and crt_type='CRT1_DB' 
    '''
    results = mysqldb.get_DB(sql_str)
    loadtimes=[]
    for row in results:
        loadtime = row[0]
        loadtimes.append(loadtime)
    return loadtimes

def get_passed_count(loadname):
    sql_str='''
    select count(*) from (
      select FROM_UNIXTIME(time_epoch_start,\"%Y-%m-%d %h:%i:%s\") AS time, 
      test_line_id, robot_ip,enb_build, test_case_name, test_status, enb_config 
      from test_results  
      where enb_build='" . $loadname . "' 
      and crt_type='CRT1_DB' and record_valid=1 and test_status='passed' group by test_case_name ) as t 
    
    '''


def main():
    crt_type= (parse_args().type)
    logger.info ('crt_type is: %s' % (crt_type) )
    object = get_loadnames(crt_type)
    for i in object:
        print(get_load_name_time(i))





    # df = pd.DataFrame(list(object))
    # print(df[1].tolist())

    # load_name_list = df[1].tolist()  #loadname  list
    # for i in range(len(load_name_list)):
    #     load_name=load_name_list[i]
    #     print (load_name)


    # loadnames=[]
    # loadtimes=[]
    # for row in object:
    #     loadtime = row[0]
    #     loadname = row[1]
    #     loadnames.append(loadname)
    #     loadtimes.append(loadtime)
    #
    # for i in range(len(object)):
    #     print(loadnames[i])
    #     crt_load_time=loadtimes[i]
    #     crt_load_name=loadnames[i]




    # sql_str= ""
    # mysqldb.get_DB(sql_str)


if __name__ == "__main__":
    t_start = datetime.now()  # 起x始时间
    logger = set_log_level('INFO')
    logger.info('%s Start running %s' % ('-' * 10, '-' * 10))
    mysqldb = Pymysql()
    main()
    mysqldb.close_DB()
    t_end = datetime.now()  # 关闭时间
    time = (t_end - t_start).total_seconds()
    logger.info('The script run time is: %s sec' % (time))
