#-*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
url = 'http://laibaoqin.top/ranzhi/www'
user = 'admin'
password = 12345678

class Test_ranzhi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_case1(self):
        """48548"""
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(url)
        text = self.driver.find_element_by_css_selector(".btn").text
        print(text)
        if text != "繁體":  # 选择系统语言
            self.driver.find_element_by_css_selector(".btn").click()
            self.driver.find_element_by_xpath("//*[text()='繁體']").click()

        self.driver.find_element_by_css_selector("#account").send_keys(user)
        self.driver.find_element_by_css_selector("#password").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='keepLoginon']").click()

        self.driver.find_element_by_css_selector('#submit').click()
        time.sleep(1)
        try:
            print(self.driver.find_element_by_class_name('bootbox-body').text)
            self.driver.find_element_by_xpath('//button[@data-bb-handler="ok"]').click()
        except:
            pass
        try:
            act_name = self.driver.find_elements_by_css_selector(".nav.navbar-nav>li>a")[0].text
            print(act_name)
            assert act_name == "admin"
        except Exception as e:
            print("验证出错了", e)

        print("233")
        self.assertEqual(1 ,2)