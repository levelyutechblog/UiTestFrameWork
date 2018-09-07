# -*- coding: utf-8 -*-
import psycopg2
import os
from config import *
import subprocess

class pgSql:

    def __init__(self,host,user,pwd,db,port=None):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.port = port

    def __GetConnect(self):
        """
            get database connection
        """
        if not self.db:
            raise (NameError, "Database_name error")
        if self.port is not None:
            self.conn = psycopg2.connect(database=self.db, user=self.user, password=self.pwd, host=self.host, port=self.port)
        else:
            self.conn = psycopg2.connect(database=self.db, user=self.user, password=self.pwd, host=self.host)
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "cur error")
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

        self.conn.commit()
        self.conn.close()
        return resList


    def ExecNonQuery(self, sql):
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
