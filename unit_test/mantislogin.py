# coding=utf-8
from yoyotestui.data.datainfo import *
from selenium import webdriver
from yoyotestui.page.login_public import Login
from yoyotestui.base.base import BasePage
import unittest

class Mantis_login(unittest.TestCase):
        """ 测试类  """
        def setUp(self):
            fp = webdriver.FirefoxProfile(path)
            self.driver = webdriver.Firefox(fp)
            self.Login_test1 = Login(self.driver)
            self.Login_test1.login_step()
            self.Login_test1.V_login()
        def tearDown(self):
            #self.Login_test1.login_out()
            pass
        def test_case1(self):
            broswer = BasePage(self.driver)
            loc = ("xpath","//*[@id='dropdown_projects_menu']/a")
            name =  broswer.get_text(loc)
            print(name)
            if  name != "拉耳机":
                broswer.click(loc)
                loc_Targe = ("link text","拉耳机")
                broswer.click(loc_Targe)
            # 点击提交问题
            loc_commit = ("css selector",".menu-icon.fa.fa-edit")
            broswer.click(loc_commit)
            #
            loc_









if __name__ == "__main__":

    unittest.main()