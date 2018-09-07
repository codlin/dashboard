#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/25 9:28
# @Author : Ma xiaoquan
# @Email : xiaoquan.ma@nokia-sbell.com
# @Site : 
# @File : index.py
# @desc:

import json
import requests
from datetime import datetime
import pandas as pd
import pymysql
import csv
import codecs
import time


# 时间戳转换日期
def timestamp_datetime(ts):
    if isinstance(ts, (int, float, str)):
        try:
            ts = int(ts)
        except ValueError:
            raise
        if len(str(ts)) == 13:
            ts = int(ts / 1000)
        if len(str(ts)) != 10:
            raise ValueError
    else:
        raise ValueError()
    d = datetime.fromtimestamp(ts)
    result = d.strftime("%Y-%m-%d %H:%M:%S")
    return result


# 从Jenkins获取原始数据
def get_jenkins_data(url):
    response = requests.get(url)
    healthCheckup = response.text
    healthCheckupPython = json.loads(healthCheckup)
    return healthCheckupPython


# 获取整合后checksite数据
def Get_New_Check_Site(url):
    # checksite section
    checksite = get_jenkins_data(url)  # dict
    # print checksite
    length = len(checksite['allBuilds'])  # 2549

    checksite_lis = list()  # 创建一个空list,
    for i in range(0, length):
        displayName = checksite['allBuilds'][i]['displayName']
        JobStatus = checksite['allBuilds'][i]['result']
        TimeStamp = checksite['allBuilds'][i]['timestamp']
        TimeStamp = timestamp_datetime(str(TimeStamp))
        dic_item = displayName.split('_')

        if len(dic_item) == 7:
            # print i
            ip = dic_item[1].replace('"', '')  # 字符串去双引号
            Loadname = dic_item[2] + '_' + dic_item[3] + '_' + dic_item[4] + '_' + dic_item[5] + '_' + dic_item[6]
            jenkins_job_id = dic_item[0].replace('#','')
            # print jenkins_job_id
            newdict = dict(checksite_id=jenkins_job_id,loadname=Loadname, ip=ip, checksite_time=TimeStamp, checksite_status=JobStatus)
            # print newdict
            newdict = str(newdict)
            checksite_lis.append(newdict)
    return checksite_lis


# 获取整合后healthcheck数据
def Get_New_Health_Check(url):
    # health check section
    healthcheck = get_jenkins_data(url)  # dict
    # print checksite
    length = len(healthcheck['allBuilds'])  # 2549

    healthcheck_lis = list()  # 创建一个空list,
    for i in range(0, length):
        displayName = healthcheck['allBuilds'][i]['displayName']
        JobStatus = healthcheck['allBuilds'][i]['result']
        TimeStamp = healthcheck['allBuilds'][i]['timestamp']
        TimeStamp = timestamp_datetime(str(TimeStamp))
        dic_item = displayName.split('_')

        if len(dic_item) == 7:
            # ip = eval(dic_item[1])  # 字符串去双引号
            ip = dic_item[1].replace('"', '')
            loadname = dic_item[2] + '_' + dic_item[3] + '_' + dic_item[4] + '_' + dic_item[5] + '_' + dic_item[6]
            jenkins_job_id = dic_item[0].replace('#', '')
            newdict = dict(healthcheck_id=jenkins_job_id,loadname=loadname, ip=ip, healthcheck_time=TimeStamp, healthcheck_status=JobStatus)
            newdict = str(newdict)
            # print newdict
            healthcheck_lis.append(newdict)
    return healthcheck_lis


# 获取整合后upgrade数据
def Get_New_Upgrade(url):
    # health check section
    upgrade = get_jenkins_data(url)  # dict
    # print checksite
    length = len(upgrade['allBuilds'])  # 2549

    upgrade_lis = list()  # 创建一个空list,
    for i in range(0, length):
        displayName = upgrade['allBuilds'][i]['displayName']
        JobStatus = upgrade['allBuilds'][i]['result']
        TimeStamp = upgrade['allBuilds'][i]['timestamp']
        TimeStamp = timestamp_datetime(str(TimeStamp))
        dic_item = displayName.split('_')

        if len(dic_item) == 7:
            # print i
            ip = dic_item[1].replace('"', '')  # 字符串去双引号
            loadname = dic_item[2] + '_' + dic_item[3] + '_' + dic_item[4] + '_' + dic_item[5] + '_' + dic_item[6]
            jenkins_job_id = dic_item[0].replace('#', '')
            newdict = dict(upgrade_id=jenkins_job_id,loadname=loadname, ip=ip, upgrade_time=TimeStamp, upgrade_status=JobStatus)
            # print newdict
            newdict = str(newdict)
            upgrade_lis.append(newdict)
    return upgrade_lis

#获取mysql连接
def get_conn():
    conn = pymysql.connect(host='135.242.139.122', port=33306, user='root', passwd='123456', db='crt_auto', charset='utf8')
    return conn


def insert(cur, sql, args):
    cur.execute(sql, args)

def truncate():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('truncate fzm_fdd_testline')
    conn.commit()
    cur.close()
    conn.close()

def read_csv_to_mysql(filename):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into fzm_fdd_testline values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for item in reader:
            if item[1] is None or item[1] == '':  # item[1]作为唯一键，不能为null
                continue
            args = tuple(item)
            # print(args)
            insert(cur, sql=sql, args=args)

        conn.commit()
        cur.close()
        conn.close()


def main():
    checksite_url_nj = 'http://135.242.139.122:8085/view/AICT_3_FDD/job/check_site_state_FDD_AICT3/api/json?tree=allBuilds[result,displayName,timestamp]'
    checksite_url_usa = 'http://10.52.200.190/view/AICT_3_FDD/job/check_site_state_FDD_AICT3/api/json?tree=allBuilds[result,displayName,timestamp]'

    healthCheckup_url_nj = 'http://135.242.139.122:8085/view/AICT_3_FDD/job/healthCheckup_AICT3_FDD/api/json?tree=allBuilds[result,displayName,timestamp]'
    healthCheckup_url_usa = 'http://10.52.200.190/view/AICT_3_FDD/job/healthCheckup_AICT3_FDD/api/json?tree=allBuilds[result,displayName,timestamp]'

    upgrade_url_nj = 'http://135.242.139.122:8085/view/AICT_3_FDD/job/upgrade_FDD_AICT3/api/json?tree=allBuilds[result,displayName,timestamp]'
    upgrade_url_usa = 'http://10.52.200.190/view/AICT_3_FDD/job/upgrade_FDD_AICT3/api/json?tree=allBuilds[result,displayName,timestamp]'

    # 调用整合的数据
    Obj_checksite = Get_New_Check_Site(checksite_url_nj) + Get_New_Check_Site(checksite_url_usa)  # list object
    # 将列表中的元素转成字典
    for i in range(0, len(Obj_checksite)):
        Obj_checksite[i] = eval(Obj_checksite[i])
    # pandas读取数据
    columns = ['loadname','ip','checksite_id','checksite_time','checksite_status']
    df_checksite = pd.DataFrame(Obj_checksite, columns=columns)
    # print(df_checksite)

    Obj_healthcheck = Get_New_Health_Check(healthCheckup_url_nj) + Get_New_Health_Check(healthCheckup_url_usa)
    for i in range(0, len(Obj_healthcheck)):
        Obj_healthcheck[i] = eval(Obj_healthcheck[i])
    columns = ['healthcheck_id','loadname', 'ip', 'healthcheck_time', 'healthcheck_status']
    df_healcheck = pd.DataFrame(Obj_healthcheck, columns=columns)
    # print df_healcheck

    Obj_upgrade = Get_New_Upgrade(upgrade_url_nj) + Get_New_Upgrade(upgrade_url_usa)
    for i in range(0, len(Obj_upgrade)):
        Obj_upgrade[i] = eval(Obj_upgrade[i])
    columns = ['upgrade_id','loadname', 'ip', 'upgrade_time', 'upgrade_status']
    df_upgrade =  pd.DataFrame(Obj_upgrade, columns=columns)
    # print df_upgrade

    # 两个表合并
    result_1 = pd.merge(df_checksite,df_healcheck,on=['loadname','ip'])
    result_2 = pd.merge(result_1,df_upgrade,on=['loadname','ip'])

    # 保存到csv文件
    result_2.to_csv('fzm_fdd_result.csv')

    # 保存到csv文件
    time.sleep(3)
    truncate()
    time.sleep(1)
    read_csv_to_mysql('fzm_fdd_result.csv')



if __name__ == '__main__':
    t_start = datetime.now()  # 起x始时间
    # 保存到csv文件
    main()
    t_end = datetime.now()  # 关闭时间
    print "The script run time is:" , (t_end - t_start).total_seconds()  # 程序运行时间