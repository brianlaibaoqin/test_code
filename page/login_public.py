# coding=utf-8
from selenium import webdriver
from yoyotestui.data.datainfo import *
from yoyotestui.base.base import BasePage

class  Login(object):
    """网站公用登录类"""
    def __init__(self,driver):
        self.driver = driver
        self.broswer = BasePage(self.driver )
        self.broswer.open(url)
    def login_step(self):
        loc = ("css selector","#username")
        self.broswer.send_keys(loc ,username)
        loc1 = ("xpath","//input[@type='submit']")
        self.broswer.click(loc1)
        loc2 = ("css selector","#password")
        self.broswer.send_keys(loc2,password)
        self.broswer.click(loc1)
    def V_login(self):
        loc_name = ("css selector",".breadcrumb>li>a")
        v_username = self.broswer.get_text(loc_name)
        assert v_username == "administrator ( brianlai )"
        print("登录测试成功", v_username)
    def login_out(self):
        self.driver.quit()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    a = Login(driver)
    a.login_step()
    a.V_login()
    a.login_out()




























