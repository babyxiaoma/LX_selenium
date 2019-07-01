from selenium import webdriver
from base.find_element import Driver_Emelent
import time


class ActionMethod(object):
    def open_browser(self, *args):
        '''打开浏览器'''
        browser = args[0]
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'ie':
            self.driver = webdriver.Edge()
        else:
            self.driver = webdriver.Firefox()

    def get_url(self, *args):
        '''打开url'''
        url = args[0]
        self.driver.get(url)

    def get_title(self,*args):
        '''获取title'''
        return self.driver.title

    def get_element(self, *args):
        '''获取定位元素'''
        node = args[0]
        DE = Driver_Emelent(self.driver)
        element = DE.get_element(node=node)
        return element

    def element_send_keys(self, *args):
        '''输入操作'''
        node = args[0]
        value = args[1]
        self.get_element(node).send_keys(value)

    def element_click(self, *args):
        '''点击操作'''
        node = args[0]
        self.get_element(node).click()

    def implicitly_wait(self, *args):
        '''强制隐式等待时间10s'''
        self.driver.implicitly_wait(10)

    def sleep_time(self, *args):
        '''强制等待时间3s'''
        time.sleep(3)

    def close_browser(self, *args):
        '''关闭浏览器'''
        self.driver.close()

    def maximize_window(self, *args):
        '''最大化浏览器'''
        self.driver.maximize_window()
