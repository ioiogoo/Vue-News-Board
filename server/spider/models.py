# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 2017/1/3 15:11
'''
import sqlite3

class Sql(object):
    def __init__(self):
        self.conn = sqlite3.connect('news.db')
        self.cur = self.conn.cursor()

    def execute(self, sql=None, values=None):
        try:
            if values:
                self.cur.execute(sql, values)
            else:
                self.cur.execute(sql)
        except Exception as e:
            return 1, e
        if 'select' in sql:
            results = self.cur.fetchall()
        else:
            results = 'success'
        self.conn.commit()
        return 0, results
