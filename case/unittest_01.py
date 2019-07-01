from business.login_business import Login_Business
from selenium import webdriver
import unittest


class First_Case(unittest.TestCase):
    def setUp(self):
        '''前置条件'''
        self.driver = webdriver.Chrome()
        self.driver.get('http://ht.test.by-998.com/index/login')
        self.LB = Login_Business(driver=self.driver)

    def tearDown(self):
        '''后置条件'''
        self.driver.close()

    def test_login_succeed(self):
        '''测试登录成功'''
        error_login = self.LB.login_succeed(username='leon2017',password='passnew201')
        print(error_login)
        self.assertTrue(expr=error_login,msg='用例失败')

    def test_login_username_error(self):
        '''测试用户名错误'''
        error_username = self.LB.login_username_error(username='leon2018',password='passnew2017')
        print(error_username)
        self.assertFalse(expr=error_username, msg='用例通过')

    def test_login_password_error(self):
        '''测试密码错误'''
        error_password = self.LB.login_password_error(username='leon2017', password='passnew2018')
        print(error_password)
        self.assertFalse(expr=error_password, msg='用例通过')

    # def main(self):
    #     self.test_login_username_error()
    #     self.test_login_password_error()
    #     self.test_login_succeed()
    #     self.driver.close()

if __name__ == '__main__':
    unittest.main()
