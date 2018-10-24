#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/31 12:28
# @Author : Ma xiaoquan
# @Email : xiaoquan.ma@nokia-sbell.com
# @Site :
# @File : pydbsync.py
# @desc:

import MySQLdb as mdb
import re
import sys
import os.path
from datetime import datetime

cfg = None

if os.path.isfile("pydbconfig.py"):
	import pydbconfig
	cfg = pydbconfig.cfg
	print "Loaded from python config"
else:
	import inspect
	import yaml
	cfg = yaml.load(open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/config.yaml', 'r'))
	print "Loaded from yaml"

tablecfg = cfg["tables"]
srcparams = cfg["parameters"]["source"]
dstparams = cfg["parameters"]["destination"]
batchmax = cfg["parameters"]["batchmax"]


def countval(db, ctable, fromKey=None):
	cur = db.cursor()
	if fromKey is None:
		cur.execute("SELECT COUNT(*) FROM `" + ctable + "`")
	else:
		cur.execute("SELECT COUNT(*) FROM `" + ctable + "` WHERE `" + tablecfg[ctable]["updated-field"] + "` >= %s",
					[fromKey])

	ret = cur.fetchone()[0]
	return ret


def findAndCompareRow(row, cmpdescribe, showcreate):
	ret = False
	# Search "row" into row list (from DESCRIBE query)
	for i in range(len(cmpdescribe)):
		currow = cmpdescribe[i]
		# Found a column with the same name, comparing signature
		if currow[0] == row[0]:
			ret = True
			if len(row) != len(currow):
				print row
				print currow
				ret = False
			else:
				for j in range(len(row)):
					if j == 0:
						continue
					if row[j] != currow[j]:
						if row[j] == '' and currow[j] == 'on update CURRENT_TIMESTAMP':
							# May be a bug in SRC Host (MySQL 5.0)
							checkexpr = re.search('^\s*`'+row[0]+'`.*on update current_timestamp,?$', showcreate, re.MULTILINE|re.I)
							if checkexpr is None:
								print row
								print currow
								ret = False
						else:
							print row
							print currow
							ret = False
	return ret


def synctable(srcdb, dstdb, table, fromkey=None):
	tabledef = []
	duplicatedef = []
	datetimeWorkaround = []
	cur = srcdb.cursor()
	cur.execute("DESCRIBE `" + table + "`")
	for i in range(cur.rowcount):
		row = cur.fetchone()
		tabledef.append("%s")
		duplicatedef.append("`" + row[0] + "`=VALUES(`" + row[0] + "`)")
		datetimeWorkaround.append(row[1])

	# Sync all
	recordsToSync = countval(srcdb, table, fromkey)
	currentRecord = 0
	while currentRecord < recordsToSync:
		maxRecordToSync = min(recordsToSync, batchmax)
		print "Max Batch: " + str(maxRecordToSync) + " values; " + str(recordsToSync) + " in total, remaining: " \
			  + str(recordsToSync - currentRecord)
		cur = srcdb.cursor()
		dstcur = dstdb.cursor()
		if fromkey is None:
			cur.execute("SELECT * FROM `" + table + "` ORDER BY `" + tablecfg[table]["updated-field"]
						+ "` ASC LIMIT " + str(currentRecord) + "," + str(maxRecordToSync))
		else:
			cur.execute("SELECT * FROM `" + table + "` WHERE `" + tablecfg[table]["updated-field"] \
						+ "` >= %s ORDER BY `" + tablecfg[table]["updated-field"]
						+ "` ASC LIMIT " + str(currentRecord) + "," + str(maxRecordToSync), [fromkey])

		for i in range(cur.rowcount):
			row = list(cur.fetchone())
			print i
			for j in range(0, len(row)):
				if row[j] is None and (datetimeWorkaround[j] == "datetime" or datetimeWorkaround[j] == "timestamp"):
					row[j] = "0000-00-00 00:00:00"

			q = "INSERT INTO `" + table + "` VALUES (" + ",".join(tabledef) + ") ON DUPLICATE KEY UPDATE " \
				+ ",".join(duplicatedef)
			dstcur.execute(q, row)

		# if len(dstcur.messages) > 0:
		# 	print row
		currentRecord += cur.rowcount


def main():
	currentTable = ""
	srcdb = None
	dstdb = None
	try:
		srcdb = mdb.connect(host=srcparams["host"], user=srcparams["user"], passwd=srcparams["pass"], port=srcparams["port"], db=srcparams["schema"])
		print "Connected to source host"
		dstdb = mdb.connect(host=dstparams["host"], user=dstparams["user"], passwd=dstparams["pass"], port=dstparams["port"], db=dstparams["schema"])
		print "Connected to destination host"

		for table in tablecfg:
			currentTable = table
			cur = dstdb.cursor()
			dstlast = None
			createTable = False
			try:
				cur.execute("SELECT MAX(`" + tablecfg[table]["updated-field"] + "`) FROM `" + table + "`")
				dstlast = cur.fetchone()

				# Check table schema
				dstdescribe = []
				cur = dstdb.cursor()
				cur.execute("DESCRIBE `" + table + "`")
				for i in range(cur.rowcount):
					row = cur.fetchone()
					dstdescribe.append(row)

				cur = dstdb.cursor()
				cur.execute("SHOW CREATE TABLE " + table)
				showcreate = cur.fetchone()[1]

				cur = srcdb.cursor()
				cur.execute("DESCRIBE `" + table + "`")

				# if cur.rowcount != len(dstdescribe):
				# 	print "WARNING: structure of \"" + table + "\" table doesn't match between source and destination DB Host, dropping and recreating table"
				# 	## dstdb.cursor().execute("DROP TABLE `" + table + "`")
				# 	# dstlast = None
				# 	# createTable = True
				# else:
				# 	for i in range(cur.rowcount):
				# 		row = cur.fetchone()
				# 		if findAndCompareRow(row, dstdescribe, showcreate) == False:
				# 			print "WARNING: structure of \"" + table + "\" table doesn't match between source and destination DB Host, dropping and recreating table"
				# 			## dstdb.cursor().execute("DROP TABLE `" + table + "`")
				# 			# dstlast = None
				# 			# createTable = True

			except mdb.Error, ex:
				if ex.args[0] != 1146:
					# If other error than "table doesn't exists" (eg. errno 1146)
					raise ex
				else:
					print "Table " + table + " doesn't exists on destination host, creating now"
					# If table doesn't exists (eg. errno 1146)
					createTable = True
					pass


			# cur = srcdb.cursor()
			# cur.execute("SHOW CREATE TABLE `" + table + "`")
			# createrow = cur.fetchone()
			# dstdb.cursor().execute(createrow[1])

			# Sync only changed
			cur = srcdb.cursor()
			cur.execute("SELECT MAX(`" + tablecfg[table]["updated-field"] + "`) FROM `" + table + "`")
			srclast = cur.fetchone()

			if dstlast[0] != srclast[0]:
				print table + ": sync from " + str(dstlast[0])
				synctable(srcdb, dstdb, table, dstlast[0] - 3000)
				print table + " sync ended"
			else:
				print table + " is already sync'ed"


	except mdb.Error, e:
		print "Error %d on table %s: %s" % (e.args[0], currentTable, e.args[1])
		sys.exit(1)
	finally:
		if srcdb is not None:
			srcdb.close()
		if dstdb is not None:
			dstdb.close()


if __name__ == '__main__':
	t_start = datetime.now()  # 起x始时间
	main()
	t_end = datetime.now()  # 关闭时间
	print "The script run time is:", (t_end - t_start).total_seconds()  # 程序运行时间