# coding=utf-8

from selenium import webdriver
from yoyotestui.base.base import BasePage
import unittest


class Mantis_login(unittest.TestCase):
    """ 测试类  """
    def setUp(self):
        url  = "http://104.129.184.199/mantis/login_page.php"
        path = r"C:\Users\baoqin.lai\AppData\Roaming\Mozilla\Firefox\Profiles\om8guvhh.default"
        fp = webdriver.FirefoxProfile(path)
        self.driver = webdriver.Firefox(fp )
        self.broswer = BasePage(self.driver)
        self.broswer.open(url )

    def tearDown(self):
        self.driver.quit()

    def test_case1(self):
        loc = ("css selector","#username")
        self.broswer.send_keys(loc ,"administrator")
        loc1 = ("xpath","//input[@type='submit']")
        self.broswer.click(loc1)
        loc2 = ("css selector","#password")
        self.broswer.send_keys(loc2,"a124689a")
        self.broswer.click(loc1)
        loc_name = ("css selector",".breadcrumb>li>a")
        v_username = self.broswer.get_text(loc_name)
        print("登录测试成功",v_username)
        self.assertIn (v_username ,"administrator ( brianlai )")


if __name__ == "__main__":
    unittest.main()