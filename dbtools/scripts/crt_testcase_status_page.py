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
from common.logger import logger, set_log_level  # noqa: E402
from scripts.mysql import Pymysql  # noqa: E402

mysqldb = Pymysql()


def parse_args():
    p = argparse.ArgumentParser(
        description='Request CRT data of project from mysql database',
        usage="%(prog)s [OPTION]... (type '-h' or '--help' for help)")
    p.add_argument(
        '-t',
        '--type',
        action='store',
        default='FLF',
        help="Get the project type of CRT")
    args = p.parse_args()
    return args


def get_loadnames(mode):
    """
    :param mode: FZM FDD = FLF
                 FZM TDD = TLF
                 CFZC FDD = FLC
                 CFZC TDD = TLC
    :return loadname list
    example: get_loadname('FLF')
    """
    crt_type = str(mode) + '%'
    logger.debug('Type is: %s', mode)
    logger.debug('crt_type is: %s', crt_type)
    sql_str = '''SELECT enb_build
FROM test_results 
WHERE enb_build !='Null' 
    AND enb_build !='' 
    AND enb_build NOT LIKE '%MF%' 
    AND crt_type='CRT1_DB' 
    AND enb_release LIKE("''' + crt_type + '''")
GROUP BY enb_build 
ORDER BY time_epoch_start DESC LIMIT 30
        '''
    try:
        data = mysqldb.get_DB(sql_str)
        results = []
        for row in data:
            loadname = row[0]
            results.append(loadname)
        return results
    except Exception, e:
        logger.debug('error: get_loadnames is %s', e)


def crt_project_type(crt_type):
    if crt_type == 'FLF':
        mode = '1'
    elif crt_type == 'TLF':
        mode = '2'
    elif crt_type == 'FLC':
        mode = '3'
    elif crt_type == 'TLC':
        mode = '4'
    else:
        mode = ''
    return mode


# ===============
# TestCase class
# ===============
class TestCaseStatus(object):
    def __init__(self, loadname, crt_type):
        self.loadname = loadname
        self.crt_type = crt_type

    # FLF17A convert FLF17ASP
    def _17asp_convert(self):
        branch = self.loadname.split('_')
        if branch[0] == "FLF17A" and branch[-3] == '1000':
            result = self.loadname.replace("FLF17A", "FLF17ASP")
        else:
            result = self.loadname
        return result

    # Get release id number
    def get_productrelease(self):
        branch = self._17asp_convert().split('_')
        result = branch[0]
        sql = "SELECT id FROM crt_productrelease WHERE crt_productrelease.release='" + result + "'"
        try:
            result = mysqldb.get_DB(sql)
            result = str(result[0][0])
            logger.debug('result is %s', result)
        except Exception, e:
            logger.error('error: get_productrelease is %s', e)
        return result

    def get_load_name_time(self):
        sql_str = '''SELECT FROM_UNIXTIME(min(time_epoch_start),'%Y-%m-%d %H:%i:%s') AS time 
FROM test_results 
WHERE enb_build="''' + self.loadname + '''" AND crt_type='CRT1_DB' '''
        try:
            data = mysqldb.get_DB(sql_str)
            result = data[0][0]
            return result
        except Exception, e:
            logger.error('error:get_load_name_time function is %s', e)

    def get_failed(self):
        sql_str = '''SELECT enb_build, test_case_name, test_line_id, robot_ip, test_status, test_suite
FROM test_results
WHERE crt_type = 'CRT1_DB' 
    AND record_valid = 1
    AND test_status!='Passed'
    AND enb_build="''' + self.loadname + '''" 
    AND test_case_name NOT IN (
        SELECT test_case_name 
        FROM test_results 
        WHERE enb_build = "''' + self.loadname + '''"  
            AND crt_type = 'CRT1_DB' 
            AND record_valid = 1
            AND test_status = 'Passed' 
        GROUP BY test_case_name ) 
GROUP BY test_case_name 
ORDER BY robot_ip'''
        try:
            results = mysqldb.get_DB(sql_str)
            return results
        except Exception, e:
            logger.error('error: get_failed function is %s', e)

    def get_passed(self):
        sql_str = '''SELECT enb_build, test_case_name, test_line_id, robot_ip, test_status, test_suite
FROM test_results  
WHERE enb_build="''' + self.loadname + '''" 
    AND crt_type = 'CRT1_DB' 
    AND test_status = 'passed' 
    AND record_valid = 1 
GROUP BY test_case_name'''
        results = mysqldb.get_DB(sql_str)
        return results

    def get_unexecuted(self):
        branch = self.get_productrelease()
        logger.debug('branch is %s', branch)
        sql_str = '''SELECT *
FROM (
    SELECT casename
    FROM crt_testcase_name
        INNER JOIN crt_testcase_release ON crt_testcase_release.case_id = crt_testcase_name.id
    WHERE crt_testcase_release.release_id = "''' + branch + '''" 
    GROUP BY casename) AS t1
WHERE t1.casename NOT IN (
    SELECT test_case_name 
    FROM test_results 
    WHERE enb_build = "''' + self.loadname + '''" 
        AND record_valid = 1 
        AND crt_type = 'CRT1_DB' 
    GROUP BY test_case_name
)'''
        try:
            results = mysqldb.get_DB(sql_str)
            logger.debug('results is : %s', results)
            return results
        except Exception, e:
            logger.error('get_testline_info is error %s ', e)

    @classmethod
    def list_to_str(cls, list_val):
        str_val = ''
        for i in range(0, len(list_val)):
            if list_val[i] is None:
                list_val[i] = 'NA'
            item = '"' + list_val[i] + '",'
            str_val = str_val + item
        result = str_val[:-1]
        return result

    # Get all platform information by testcase name
    def get_testline_info(self, tc_name):
        branch = self.get_productrelease()
        logger.debug('branch is %s', branch)
        sql = '''SELECT * 
FROM (
    SELECT crt_testcase_name.id, crt_testcase_release.release_id, crt_testcase_name.casename, 
        crt_testcase_schedule.case_id, crt_testcase_schedule.testline_id, crt_testline.`mode`, crt_testline.sitetype, 
        crt_testline.node, crt_testline.ca, crt_testline.jenkinsjob, crt_testline.mbtsid, crt_testline.mnode, 
        crt_testline.cfgid,crt_testline.product_id
    FROM crt_testcase_name 
        LEFT JOIN crt_testcase_release ON crt_testcase_name.id = crt_testcase_release.case_id 
        LEFT JOIN crt_testcase_schedule ON crt_testcase_name.id = crt_testcase_schedule.case_id 
        LEFT JOIN crt_testline ON crt_testcase_schedule.testline_id = crt_testline.id
) AS testpage
WHERE casename="''' + tc_name + '''"  AND  release_id ="''' + branch + '''" 
        '''
        # logger.debug('crt_type is %s', self.crt_type )
        logger.debug('get_testline_info sql str is : %s', sql)
        # print 'get_testline_info sql str is :', str
        try:
            results = mysqldb.get_DB(sql)
            logger.debug('results is : %s', results)
        except Exception, e:
            results = 'null'
            logger.error('get_testline_info is error %s ', e)
        return results


def running(crt_type):
    t_start = datetime.now()  # Start Time
    logger.info('%s Start running %s' % ('-' * 10, '-' * 10))
    loadnames = get_loadnames(crt_type)
    logger.debug("loadnames list is %s" % loadnames)

    for loadname in loadnames:
        logger.debug("loadname is %s" % loadname)

        testcase = TestCaseStatus(loadname, crt_project_type(crt_type))
        # Update success testcases
        data_passed = testcase.get_passed()

        # Update failed testcases
        data_failed = testcase.get_failed()

        # Update unexecuted testcases
        data_unexecuted = testcase.get_unexecuted()

        # Loop update passed testcase
        for i in range(0, len(data_passed)):
            logger.debug('data_passwd length is %s:', len(data_passed))
            item = data_passed[i]
            item = list(item)
            logger.debug('item is: %s', item)

            item = testcase.list_to_str(item)
            sql_str = '''REPLACE INTO crt_load_testcase_status_page (loadname, casename, btsid, node, result, suite) 
VALUES(''' + item + '''); '''
            logger.debug('sql_str: %s', sql_str)
            try:
                mysqldb.update_DB(sql_str)
            except Exception as e:
                logger.error('error: Loop update passed testcase is %s :', e)
            logger.debug('i: %s', i)

        # Loop update failed testcase
        for i in range(0, len(data_failed)):
            item = data_failed[i]
            item = list(item)
            logger.debug('item is: %s', item)
            item = testcase.list_to_str(item)
            sql_str = '''REPLACE INTO crt_load_testcase_status_page(loadname, casename, btsid, node, result, suite) 
VALUES(''' + item + ''');'''
            logger.debug('sql_str: %s', sql_str)
            try:
                mysqldb.update_DB(sql_str)
            except Exception as e:
                logger.error('error: Loop update failed testcase is %s :', e)

        # Loop update unexecuted testcase
        for i in range(0, len(data_unexecuted)):
            item = data_unexecuted[i]
            item = list(item)
            item = testcase.list_to_str(item)

            # Get platform information by use case name
            testcase_name = item.strip('"')
            try:
                testline_info_list = testcase.get_testline_info(testcase_name)
                if testline_info_list:
                    btsid = testline_info_list[0][11]
                    jenkinsjob = testline_info_list[0][6]
                    suite = testline_info_list[0][7]

                    item = '"' + str(loadname) + '","' + str(
                        testcase_name) + '","' + str(btsid) + '","' + str(
                        jenkinsjob) + '","NUll",' + '"' + str(suite) + '"'
                    logger.debug('item is: %s', item)
                    sql_str = '''REPLACE INTO crt_load_testcase_status_page
    (loadname, casename, btsid, node, result, suite)
VALUES(''' + item + ''');'''
                    logger.debug('sql_str is: %s', sql_str)

                    try:
                        mysqldb.update_DB(sql_str)
                    except Exception as e:
                        logger.error('error: Loop update unexecuted testcase is  %s :', e)
                else:
                    logger.error('loadname is %s', loadname)
                    logger.error('testcase_name is %s ', testcase_name)
                    logger.error('testline_info_list is null')
            except Exception, e:
                logger.error('testline_info_list is error %s', e)

    t_end = datetime.now()  # end time
    time = (t_end - t_start).total_seconds()
    logger.info('The script run time is: %s sec' % (time, ))


def main():
    set_log_level("DBTools", "INFO")
    logger.info('load testcases status task began.')
    list_project = ['FLF', 'TLF', 'FLC', 'TLC']
    # list_project = ['FLF']
    for i in range(len(list_project)):
        logger.info('Project is  %s ', list_project[i])
        running(list_project[i])
    logger.info('load testcases status task done.')


if __name__ == "__main__":
    main()
