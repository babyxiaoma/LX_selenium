from business.login_business import Login_Business
from selenium import webdriver
from util.read_excel import Read_Excel
import unittest
import ddt
import os
import time
from log.log import Logs


#实例化excel
ex = Read_Excel()
data = ex.get_data_list()

@ddt.ddt
class First_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = Logs()
        cls.logger = cls.log.user_log()
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://ht.test.by-998.com/index/login')

    def setUp(self):
        '''前置条件'''
        self.LB = Login_Business(driver=self.driver)

    def tearDown(self):
        '''后置条件'''
        time.sleep(2)
        #此方法获取到用例error时候截图待调整
        for method_name,error in self._outcome.errors:
            if error:
                print(error)
                case_name = self._testMethodName
                filename = os.path.join(os.getcwd()+'/report/'+case_name+'.png' )
                self.driver.save_screenshot(filename=filename)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.logger.close_handle()


    # @ddt.data(
    #     ['leon2017','passnew2017','login_succeed','请输入您的登录信息'],
    #     ['leon2018', 'passnew2017','username_error','用户名或密码错误'],
    #     ['leon2017', 'passnew2018','username_error','用户名或密码错误']
    # )

    @ddt.data(*data)
    def test_register_case(self,data):
        username, password, assertCode, assertText = data
        print(data)
        self.logger.info('the is a 用例')
        error_register = self.LB.register_function(username,password,assertCode,assertText)
        self.assertFalse(error_register,'测试失败')



if __name__ == '__main__':
    unittest.main()
