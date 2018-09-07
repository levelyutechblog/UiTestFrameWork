# -*- coding: utf-8 -*-
import pymssql
import os

class MsSql:

	def __init__(self,host,user,pwd,db,port=None):
		self.host = host
		self.user = user
		self.pwd = pwd
		self.db = db
		self.port = port

	def __GetConnect(self):
		"""

		"""
		if not self.db:
			raise(NameError,"error")
		if self.port is not None:
			self.conn = pymssql.connect(host=self.host,port=self.port, user=self.user,password=self.pwd,database=self.db,charset="utf8")
		else:
			self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
		cur = self.conn.cursor()
		if not cur:
			raise(NameError,"error")
		else:
			return cur

	def ExecQuery(self, sql):
		"""
			ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
			resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
			for (id,NickName) in resList:
				print str(id),NickName
		"""
		cur = self.__GetConnect()
		cur.execute(sql)
		resList = cur.fetchall()

		self.conn.close()
		return resList

	def ExecNonQuery(self,sql):
		"""
		"""
		cur = self.__GetConnect()
		cur.execute(sql)
		self.conn.commit()
		self.conn.close()

	def ExecProc(self, proc, *args):
		try:
			cur = self.__GetConnect()
			cur.execute(proc, args)
			self.conn.commit()
		except Exception as e:
			raise Exception(e)
		finally:
			self.conn.close()


def get_sql(script_file):
	if os.path.exists(script_file):
		with open(script_file, 'r+') as fd:
			buff = fd.read()
		return buff
	else:
		raise AttributeError("没有这个文件 : %s" % script_file)