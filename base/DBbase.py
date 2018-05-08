# coding:utf-8
'''
@author: crazyant.net
@version: 2013-10-22

封装的mysql常用函数
'''

from test_code.base.mySQLDB import DB
from test_code.data.datainfo import *


class Deluser():
    def __init__(self):
        self.db = DB('120.79.13.73', 3306, 'root', 'root', 'ymtest')
    def delusername(self):
        self.db.update(strSql)

if __name__ == "__main__":
    aaa = Deluser()
    aaa.delusername()










