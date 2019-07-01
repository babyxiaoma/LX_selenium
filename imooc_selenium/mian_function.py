from selenium import webdriver
from base.find_element import Driver_Emelent
import time


class Funtion(object):
    def __init__(self,url):
        self.driver = self.get_driver(url=url)

    def get_driver(self,url):
        '''获取driver并打开url'''
        driver = webdriver.Chrome()
        driver.get(url=url)
        driver.maximize_window()
        return driver


    def get_user_element(self,node):
        '''获取element'''
        get_element = Driver_Emelent(self.driver)
        user_element = get_element.get_element(node=node)
        return user_element

    def send_info(self,node,data):
        '''输入用户信息'''
        self.get_user_element(node=node).send_keys(data)


    def main(self):
        #输入账号
        self.send_info(node='username',data='leon2017')
        #输入密码
        self.send_info(node='password',  data='passnew201')
        #获取登录前title
        title1 = self.driver.title
        #点击登录按钮
        self.get_user_element(node='button',).click()
        time.sleep(3)
        #判断登录后的title是否与登录前的一致,不一致登录失败保存截图
        if self.driver.title != title1:
            print('登录成功!')
        else:
            self.driver.save_screenshot(filename='E:/LX_selenium/imooc_selenium/user_error.png')
        #等待三秒
        time.sleep(3)
        #关闭浏览器
        self.driver.close()

if __name__ == '__main__':
    test = Funtion('http://ht.test.by-998.com/index/login')
    test.main()
