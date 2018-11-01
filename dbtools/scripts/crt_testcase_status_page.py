#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ma xiaoquan
# @Contact: xiaoquan.ma@nokia-sbell.com
# @File: crt_testcase_status_page_old.py
# @Time: 2018/10/12 11:08
# @Desc:

import argparse
import os
import sys
from datetime import datetime

import urllib3

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

class TestCase_Status(object):

    def __init__(self, loadname):
        self.loadname = loadname

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
        order by time_epoch_start desc limit 30
        '''
        data = mysqldb.get_DB(sql_str)
        results = []
        for row in data:
            loadname = row[0]
            results.append(loadname)
        return results

    def get_release(self):
        branch = self.loadname.split('_')
        result = branch[0] + '_' + branch[1] + '_' + branch[2]
        return result

    def get_load_name_time(self):
        sql_str = '''
        select FROM_UNIXTIME(min(time_epoch_start),'%Y-%m-%d %H:%i:%s') AS time 
        from test_results where enb_build="''' + self.loadname + '''" and crt_type='CRT1_DB' 
        '''
        data = mysqldb.get_DB(sql_str)
        result = data[0][0]
        return result

    def get_failed(self):
        sql_str = '''
                select enb_build, test_case_name, test_line_id, robot_ip, test_status, test_suite
                from test_results
                where crt_type='CRT1_DB' and record_valid=1  and test_status!='Passed' and enb_build="''' + self.loadname + '''" and test_case_name
                not in(
                select test_case_name from test_results where enb_build="''' + self.loadname + '''"  and crt_type='CRT1_DB' and record_valid=1
                and test_status='Passed' group by test_case_name ) group by test_case_name order by robot_ip
        '''
        results = mysqldb.get_DB(sql_str)
        return results

    def get_passed(self):
        sql_str = '''
        select  enb_build, test_case_name, test_line_id, robot_ip, test_status, test_suite from test_results  
        where enb_build="''' + self.loadname + '''" 
        and crt_type='CRT1_DB' and test_status='passed' and record_valid=1  group by test_case_name  
        '''
        results = mysqldb.get_DB(sql_str)
        return results

    def get_unexecuted(self):
        branch = self.get_release()
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
                                          WHERE enb_build = "''' + self.loadname + '''" 
                                            AND record_valid = 1
                                            AND crt_type = 'CRT1_DB'
                                          GROUP BY test_case_name)
         '''
        results = mysqldb.get_DB(sql_str)
        return results

    def list_to_str(self, list):
        str = ''
        for i in range(0, len(list)):
            if list[i] is None:
                list[i] = 'NA'
            item = '"' + list[i] + '",'
            str = str + item
        result = str[:-1]
        return result

    # 根据testcase name 来获取全部平台信息
    def get_testline_info(self, tc_name):
        str = '''
            select * from 
            (SELECT crt_testcase_name.id, crt_testcase_name.casename, crt_testcase_schedule.case_id, crt_testcase_schedule.testline_id,
            crt_testline.`mode`,crt_testline.sitetype, crt_testline.node,crt_testline.ca,crt_testline.jenkinsjob,crt_testline.mbtsid,
            crt_testline.mnode,crt_testline.cfgid,crt_testline.product_id
            FROM crt_testcase_name 
            left JOIN crt_testcase_schedule ON crt_testcase_name.id = crt_testcase_schedule.case_id 
            left JOIN crt_testline ON crt_testcase_schedule.testline_id= crt_testline.id) as testpage
            where casename="''' + tc_name + '''"
        '''
        results = mysqldb.get_DB(str)
        return results

def running(crt_type):
    t_start = datetime.now()  # 起x始时间
    # urllib3.getproxies = lambda: {}  # 设置代理
    logger.info('%s Start running %s' % ('-' * 10, '-' * 10))

    loadnames = TestCase_Status.get_loadnames(crt_type)
    for loadname in loadnames:
        logger.debug("loadname is %s" % loadname)
        testcase = TestCase_Status(loadname)
        # 更新成功的用例
        data_passed = testcase.get_passed()

        # 更新失败的用例
        data_failed = testcase.get_failed()

        # 更新未执行的用例
        data_unexecuted = testcase.get_unexecuted()

        # 循环输出passwd的testcase，更新入数据库
        for i in range(0, len(data_passed)):
            logger.debug('data_passwd length is %s:', len(data_passed))
            item = data_passed[i]
            item = list(item)
            logger.debug('item is: %s', item)

            item = testcase.list_to_str(item)
            sql_str = '''
                REPLACE INTO crt_load_testcase_status_page(loadname,casename,btsid,node,result,suite) VALUES(''' + item + ''');
            '''
            logger.debug('sql_str: %s', sql_str)
            try:
                mysqldb.update_DB(sql_str)
            except Exception as e:
                print('update data failed is :', e)
            logger.debug('i: %s:', i)

        # 循环输出failed的testcase，更新入数据库
        for i in range(0, len(data_failed)):
            item = data_failed[i]
            item = list(item)
            logger.debug('item is: %s', item)
            item = testcase.list_to_str(item)
            sql_str = '''
                REPLACE INTO crt_load_testcase_status_page(loadname,casename,btsid,node,result,suite) VALUES(''' + item + ''');
            '''
            logger.debug('sql_str: %s', sql_str)
            try:
                mysqldb.update_DB(sql_str)
            except Exception as e:
                print('update data failed is :', e)

        # 循环输出unexecuted的testcase，更新入数据库
        for i in range(0, len(data_unexecuted)):
            item = data_unexecuted[i]
            item = list(item)
            item = testcase.list_to_str(item)

            # 根据用例名字获取平台信息
            # print(item)
            testcase_name = item.strip('"')
            testline_info_list = testcase.get_testline_info(testcase_name)
            btsid = testline_info_list[0][11]
            jenkinsjob = testline_info_list[0][6]
            suite = testline_info_list[0][7]

            item = '"' + str(loadname) + '","' + str(testcase_name) + '","' + str(btsid) + '","' + str(
                jenkinsjob) + '","NUll",' + '"' + str(suite) + '"'
            # logger.debug('item is:', item)
            sql_str = '''
                REPLACE INTO crt_load_testcase_status_page(loadname,casename,btsid,node,result,suite) VALUES(''' + item + ''');
            '''
            # logger.debug('sql_str:', sql_str)

            try:
                mysqldb.update_DB(sql_str)
            except Exception as e:
                print('update data failed is :', e)

    t_end = datetime.now()  # 关闭时间
    time = (t_end - t_start).total_seconds()
    logger.info('The script run time is: %s sec' % (time))

def main():
    logger.info('load testcases status task began.')
    list_project = ['FLF', 'TLF', 'FLC', 'TLC']
    for i in range(len(list_project)):
        running(list_project[i])

    logger.info('load testcases status task done.')

if __name__ == "__main__":
    crt_type = (parse_args().type)
    logger.info('crt_type is: %s', crt_type)
    set_log_level("DBTools", "INFO")
    main()