# -*- coding: utf-8 -*-
import psycopg2
from config import *
import os
from util.pg_db import pgSql

def insert_script():
	file_path = "{0}\\{1}\\{2}".format(os.getcwd(), SetupInfo.DATA_INIT_PATH,SetupInfo.CREATE_PROC_SCRIPT)
	data_script = open(file_path).read()
	conn = psycopg2.connect(database=SetupInfo.DB_DATABASE, user=SetupInfo.DB_USER, password=SetupInfo.DB_PWD, host=SetupInfo.DB_HOST, port=SetupInfo.DB_PORT)
	cur = conn.cursor()
	cur.execute(data_script)
	conn.commit()
	conn.close()

def insert_accountScript():
	file_path = "{0}\\{1}\\{2}".format(os.getcwd(), SetupInfo.DATA_INIT_PATH, SetupInfo.CREATE_ACCOUNT_SCRIPT)
	data_script = open(file_path).read()
	pg_platdb = psycopg2.connect(database=SetupInfo.DB_PLA_DATABASE, user=SetupInfo.DB_PLA_USER, password=SetupInfo.DB_PLA_PWD, host=SetupInfo.DB_PLA_HOST, port=SetupInfo.DB_PLA_PORT)
	cur = pg_platdb.cursor()
	cur.execute(data_script)
	pg_platdb.commit()
	pg_platdb.close()

def custom_setup():

	insert_script()
	init_data_by_script('SYSTEM_INIT')
	insert_accountScript()

def init_data_by_script(module_name, dbname = 'DB', *args):

	if dbname == 'DB':
		pgdb = pgSql(db=SetupInfo.DB_DATABASE, user=SetupInfo.DB_USER, pwd=SetupInfo.DB_PWD, host=SetupInfo.DB_HOST, port=SetupInfo.DB_PORT)
		if not hasattr(SetupInfo, module_name):
			raise AttributeError("Module: %s is not defined in SetupInfo" % module_name)
		else:
			query = getattr(SetupInfo, module_name)
		pgdb.ExecProc(query, *args)
	else:
		pgdb = pgSql(db=SetupInfo.DB_PLA_DATABASE, user=SetupInfo.DB_PLA_USER, pwd=SetupInfo.DB_PLA_PWD, host=SetupInfo.DB_PLA_HOST, port=SetupInfo.DB_PLA_PORT)
		if not hasattr(SetupInfo, module_name):
			raise AttributeError("Module: %s is not defined in SetupInfo" % module_name)
		else:
			query = getattr(SetupInfo, module_name)
		return pgdb.ExecQuery(query)


