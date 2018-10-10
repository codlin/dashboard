#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ma xiaoquan
# @Contact: xiaoquan.ma@nokia-sbell.com
# @File: mysql.py
# @Time: 2018/9/6 16:00
# @Desc:

import pymysql
import logging

logger = logging.getLogger()


class Pymysql(object):
    def __init__(self):
        self.conn_DB()

    def __del__(self):
        self.close_DB()

    # 连接数据库函数
    def conn_DB(self):
        try:
            self.conn = pymysql.connect(host='10.66.11.20', port=33306, user='root', passwd='123456', db='crt_db',
                                        charset='utf8')
            cur = self.conn.cursor()
            logger.info("mysql connect success.")
            return (self.conn, cur)

        except pymysql.Error as e:
            logger.error(e)
            print(e)

    def get_DB(self, sql_str):
        """
        :param sql_str: 查询sql语句
        """
        try:
            cursor = self.conn.cursor()  # 获取cursor
            cursor.execute(sql_str)  # 执行sql
            result = cursor.fetchall()  # 拿到结果
            logger.debug(result)
            return result  # 返回结果
        except pymysql.Error as e:
            logger.error(e)
            print(e)

    def update_DB(self, sql_str):
        try:
            cursor = self.conn.cursor()  # 获取cursor
            cursor.execute(sql_str)  # 执行sql
            self.conn.commit()  # 提交事务
        except pymysql.Error as e:
            logger.error(e)
            print(e)
            self.conn.commit()  # 如果上面的提交有错误，那么只执行对的那一个提交
            self.conn.rollback()  # 如果有错误，就回滚

    # 关闭数据库函数
    def close_DB(self):
        try:
            if self.conn:
                self.conn.close()
                logger.info("mysql close success.")
        except pymysql.Error as e:
            logger.error(e)
            print(e)
