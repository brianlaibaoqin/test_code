# coding=utf-8
from selenium import webdriver
from time import sleep



path =r'C:\Users\brian\AppData\Roaming\Mozilla\Firefox\Profiles\zf3gw55k.default'


class  Login_ranzhi(object):
        """网站登录类"""
        def __init__(self,url):
            profile = webdriver.FirefoxProfile(path)
            self.driver = webdriver.Firefox(profile)

            self.driver.maximize_window()
            self.driver.implicitly_wait(30)
            self.driver.get(url)
            text = self.driver .find_element_by_css_selector(".btn").text
            print(text)
            if text != "繁體":  #选择系统语言
                self.driver.find_element_by_css_selector(".btn").click()
                self.driver.find_element_by_xpath("//*[text()='繁體']").click()


        def login_input(self,user,password):
            """参数化登录"""
            self.driver.find_element_by_css_selector("#account").send_keys(user)
            self.driver.find_element_by_css_selector("#password").send_keys(password)
            self.driver.find_element_by_xpath("//*[@id='keepLoginon']").click()
            self.driver.find_element_by_css_selector('#submit').click()


        def vlogin(self,user):
            """验证登录"""
            try:
                act_name = self.driver .find_elements_by_css_selector(".nav.navbar-nav>li>a")[0].text
                # act_name = self.br.find_element_by_xpath("//*[@id='mainNavbar']/div/ul[1]/li/a").text
                print(act_name)
                assert act_name == user
            except Exception as e:
                print("验证出错了",e)

        def browser_quit(self):
            sleep(5)
            self.driver.quit()

if __name__ == '__main__':
    user ='admin'
    a = Login_ranzhi(url)
    a.login_input(user,'12345678')
    a.vlogin(user)
    a.browser_quit()





























