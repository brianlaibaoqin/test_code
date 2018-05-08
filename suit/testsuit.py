# coding=utf-8
import unittest,os
#from test_code.unit_test.testcase1 import Test_ranzhi
from test_code.unit_test.test_case3 import Test_ranzhi
from test_code.unit_test.test_screenshot import case_011
from test_code.unit_test.yongmak import Hp_stu_registerpop


class  testsuit():
    """组件测试套件"""
    def __init__(self,suit):
        self.suit = suit


    def add_testSuit(self):
        self.suit.addTest(unittest.makeSuite(Test_ranzhi))
        self.suit.addTest(unittest.makeSuite(Hp_stu_registerpop))

        return self.suit



if __name__ == '__main__':
    suit = unittest.TestSuite()
    a = testsuit(suit)
    ranzhisuit = a.add_testSuit()
    runner = unittest.TextTestRunner()
    runner.run(ranzhisuit)




























