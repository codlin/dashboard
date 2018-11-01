#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ma xiaoquan
# @Contact: xiaoquan.ma@nokia-sbell.com
# @File: crt_load_status_page.py
# @Time: 2018/10/6 11:08
# @Desc:

import argparse
import json
import os
import sys
from datetime import datetime

import requests
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

def get_loadnames(mode):
    """
    :param type: FZM FDD = FLF
                 FZM TDD = TLF
                 CFZC FDD = FLC
                 CFZC TDD = TLC
    :return loadname list
    example: get_loadname('TLF')
    """
    crt_type = str(mode) + '%'
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

class LoadStatus(object):
    def __init__(self, loadname):
        self.loadname = loadname

    def get_jenkins_data(self):
        url = 'https://coop.int.net.nokia.com/ext/api/pci/build/buildinfo?buildid=' + self.loadname + ''
        response = requests.get(url, verify=False)  # verify=False去掉鉴权
        if response.status_code == 200:
            data = response.text
            results = json.loads(data)
            if results:
                results = results[0]
                return results
        else:
            raise Exception("Server returned status code '%s' with message '%s'" % (
                response.status_code, response.content))

    def get_target_value(self, key, dic, tmp_list):
        """
        :param key: 目标key值
        :param dic: JSON数据
        :param tmp_list: 用于存储获取的数据
        :return: list
        """
        if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
            return 'argv[1] not an dict or argv[-1] not an list '

        if key in dic.keys():
            tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
        else:
            for value in dic.values():  # 传入数据不符合则对其value值进行遍历
                if isinstance(value, dict):
                    # 传入数据的value值是字典，则直接调用自身
                    self.get_target_value(key, value, tmp_list)
                elif isinstance(value, (list, tuple)):
                    # 传入数据的value值是列表或者元组，则调用_get_value
                    self._get_value(key, value, tmp_list)
        return tmp_list

    def _get_value(self, key, val, tmp_list):
        for val_ in val:
            if isinstance(val_, dict):
                # 传入数据的value值是字典，则调用get_target_value
                self.get_target_value(key, val_, tmp_list)
            elif isinstance(val_, (list, tuple)):
                self._get_value(key, val_, tmp_list)  # 传入数据的value值是列表或者元组，则调用自身

    def get_key_value(self, key, value, dict):
        """
        :param key:   目标key值
        :param value: 目标key对应的value
        :param dic: JSON数据
        :return: list
        """
        for i in range(0, len(dict[0])):
            key_value = dict[0][i][key]
            # pprint("key_value: %s" % key_value)
            result = dict[0][i]
            if key_value == value:
                return result

    def get_release(self):
        branch = self.loadname.split('_')
        result = branch[0] + '_' + branch[1] + '_' + branch[2]
        return result

    def get_testcase_total(self):
        barnch = self.get_release()
        logger.debug('loadname branch is  %s' % self.get_release())
        sql_str = '''
            select count(*)
            from (SELECT crt_testcase_name.casename
                  FROM crt_testcase_release
                         INNER JOIN crt_testcase_name ON crt_testcase_name.id = crt_testcase_release.case_id
                  where crt_testcase_release.load_release = "''' + barnch + '''") as t
        '''
        data = mysqldb.get_DB(sql_str)
        result = data[0][0]
        return result

    def get_load_name_time(self):
        # print('loadname is ', self.loadname)
        sql_str = '''
        select FROM_UNIXTIME(min(time_epoch_start),'%Y-%m-%d %H:%i:%s') AS time 
        from test_results where enb_build="''' + self.loadname + '''" and crt_type='CRT1_DB' 
        '''
        data = mysqldb.get_DB(sql_str)
        result = data[0][0]
        return result

    def get_passed_count(self):
        sql_str = '''
            select count(*)
            from (select test_case_name     
                  from test_results
                  where enb_build = "''' + self.loadname + '''"
                    and crt_type = 'CRT1_DB'
                    and record_valid = 1
                    and test_status = 'passed'
                  group by test_case_name) as t
        '''
        data = mysqldb.get_DB(sql_str)
        results = data[0][0]
        return results

    def get_failed_count(self):
        sql_str = '''
            select count(*)
            from (select test_case_name
                  from test_results
                  where crt_type = 'CRT1_DB'
                    and record_valid = 1
                    and test_status != 'Passed'
                    and enb_build = "''' + self.loadname + '''"
                    and test_case_name not in(select test_case_name
                                              from test_results
                                              where enb_build = "''' + self.loadname + '''"
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

    def get_unexecuted_count(self):
        branch = self.get_release()
        logger.debug('branch is %s', branch)
        sql_str = '''                
            SELECT count(*)
            FROM (SELECT *
                  FROM (SELECT crt_testcase_name.casename
                        FROM crt_testcase_release
                               INNER JOIN crt_testcase_name ON crt_testcase_name.id = crt_testcase_release.case_id
                        WHERE crt_testcase_release.load_release = "''' + branch + '''") AS t1
                  WHERE t1.casename NOT IN (SELECT test_case_name
                                            FROM test_results
                                            WHERE enb_build = "''' + self.loadname + '''"
                                              AND record_valid = 1
                                              AND crt_type = 'CRT1_DB')) AS t2                             
         '''
        data = mysqldb.get_DB(sql_str)
        results = data[0][0]
        return results

    def get_passed_first_count(self):
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
                  and enb_build = "''' + self.loadname + '''") t1
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
                                            and enb_build = "''' + self.loadname + '''") t2)
          group by test_case_name) as t3
        '''
        data = mysqldb.get_DB(sql_str)
        results = data[0][0]
        return results

    def get_debug_result(self):
        branch = self.loadname.split('_')
        if branch[0] == "FLF18A" and branch[2] == '9999':  # Trunk的包需要FLF18A替换成FLF00
            loadname = self.loadname.replace("FLF18A", "FLF00")
        else:
            pass
        if branch[0] == "TLF18A" and branch[2] == '9999':  # Trunk的包需要TLF18A替换成FLF00
            loadname = self.loadname.replace("TLF18A", "TLF00")
        else:
            pass
        if branch[0] == "FLC18A" and branch[2] == '9999':  # Trunk的包需要FLC18A替换成FLC00
            loadname = self.loadname.replace("FLC18A", "FLC00")
        else:
            pass
        if branch[0] == "TLC18A" and branch[2] == '9999':  # Trunk的包需要TLC18A替换成TLC00
            loadname = self.loadname.replace("TLC18A", "TLC00")
        else:
            pass

        logger.debug('loadname is  %s :', self.loadname)

        dic = self.get_jenkins_data()

        if dic:
            list_temp = []
            dic_pci = self.get_target_value('pci', dic, list_temp)
            list_temp2 = []
            dic_children = self.get_target_value(
                'children', self.get_key_value('name', 'crt', dic_pci), list_temp2)
            dic_debug = self.get_key_value('name', 'debug', dic_children)
            if (dic_debug.get('cases')):
                dic_cases = dic_debug['cases'][0]
                debug_status = dic_cases['result']
                if debug_status == 'PASS':
                    debug_status = 'Yes'
                if debug_status == 'FAIL':
                    debug_status = 'No'
                return debug_status
            else:
                debug_status = 'NULL'
        else:
            debug_status = 'NULL'
        return debug_status

    def get_pass_rate(self, passed_count):
        # object = LoadStatus(loadname)
        testcase_total = self.get_testcase_total()
        logger.debug('testcase_total: %s', testcase_total)
        result = round(passed_count * 100 / testcase_total, 1)
        logger.debug("pass_rate1: %s" % type(result))
        return result

    def get_first_pass_rate(self, passed_count):
        # object = LoadStatus(loadname)
        testcase_total = self.get_testcase_total()
        logger.debug('testcase_total: %s', testcase_total)
        result = round(passed_count * 100 / testcase_total, 1)
        logger.debug("pass_rate2: %s" % type(result))
        return result

def running(crt_type):
    t_start = datetime.now()  # 起x始时间
    logger.info('%s Start running %s' % ('-' * 10, '-' * 10))
    loadnames = get_loadnames(crt_type)

    # object = ['FLF18A_ENB_9999_180921_001290']
    for loadname in loadnames:
        loadstatus = LoadStatus(loadname)
        logger.debug("loadname is %s" % loadname)

        load_start_time = str(loadstatus.get_load_name_time())
        logger.debug('load_start_time: %s', type(load_start_time))

        passed_count = loadstatus.get_passed_count()
        logger.debug('passed_count: %s', type(passed_count))

        passed_first_count = loadstatus.get_passed_first_count()
        logger.debug('passed_first_count: %s', type(passed_first_count))

        failed_count = str(loadstatus.get_failed_count())
        logger.debug('failed_count: %s', type(failed_count))

        unexecuted_count = str(loadstatus.get_unexecuted_count())
        logger.debug('unexecuted_count: %s', type(unexecuted_count))

        totle_count = str(loadstatus.get_testcase_total())
        logger.debug('totle_count: %s', type(totle_count))

        pass_rate = str(loadstatus.get_pass_rate(passed_count))
        logger.debug('pass_rate: %s', pass_rate)

        first_pass_rate = str(loadstatus.get_first_pass_rate(passed_first_count))
        logger.debug('first_pass_rate: %s', first_pass_rate)

        debug = loadstatus.get_debug_result()

        logger.debug('debug status is : %s', (debug))

        item = '"' + load_start_time + '","' + str(loadname) + '","' + str(passed_count) + '","' + str(
            failed_count) + '","' \
               + unexecuted_count + '","' + totle_count + '","' + \
               first_pass_rate + '","' + pass_rate + '","' + debug + '"'
        logger.debug('item: %s', item)
        sql_str = '''
            REPLACE INTO crt_loadstatus_page(start_time,
                                             loadname,
                                             passed_num,
                                             failed_num,
                                             norun_num,
                                             total_num,
                                             first_passrate,
                                             passrate,
                                             debug) VALUES(''' + item + ''');
        '''
        logger.debug('sql_str: %s', sql_str)
        try:
            mysqldb.update_DB(sql_str)
        except Exception as e:
            print('update data failed is :', e)

    t_end = datetime.now()  # 关闭时间
    time = (t_end - t_start).total_seconds()
    logger.info('The script run time is: %s sec' % (time))

def main():
    logger.info('load status task began.')
    list_project = ['FLF', 'TLF', 'FLC', 'TLC']
    # list_project = ['TLC']
    for i in range(len(list_project)):
        running(list_project[i])

    logger.info('load status task done.')

if __name__ == "__main__":
    crt_type = (parse_args().type)
    logger.info('crt_type is: %s', crt_type)
    set_log_level("DBTools", "INFO")
    main()
