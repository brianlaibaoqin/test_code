# coding=utf-8

from selenium import webdriver
from yoyotestui.base.base import BasePage

path = r"C:\Users\baoqin.lai\AppData\Roaming\Mozilla\Firefox\Profiles\om8guvhh.default"
fp = webdriver.FirefoxProfile(path)
driver = webdriver.Firefox(fp)
broswer = BasePage(driver)
url = "http://104.129.184.199/mantis/login_page.php"
broswer.open(url)
loc = ("css selector","#username")
broswer.send_keys(loc ,"administrator")
loc1 = ("xpath","//input[@type='submit']")
broswer.click(loc1)
loc2 = ("css selector","#password")
broswer.send_keys(loc2,"a124689a")
broswer.click(loc1)
loc_name = ("css selector",".breadcrumb>li>a")
v_username = broswer.get_text(loc_name)
print("登录测试成功",v_username)
assert v_username == "administrator ( brianlai )"
driver.quit()

