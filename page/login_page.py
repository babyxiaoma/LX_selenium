from base.find_element import Driver_Emelent


class Login_Page(object):
    def __init__(self, driver):
        self.DE = Driver_Emelent(driver=driver)

    def get_username_element(self):
        '''获取用户名输入框元素'''
        return self.DE.get_element( node='username')

    def get_password_element(self):
        '''获取密码输入框元素'''
        return self.DE.get_element(node='password')

    def get_login_button_element(self):
        '''获取登录按钮元素'''
        return self.DE.get_element(node='login_button')

    def get_error_button_element(self):
        '''获取错误提示框按钮元素'''
        return self.DE.get_element(node='error_button')

    def get_login_succeed_element(self):
        '''获取登录成功文本元素'''
        return self.DE.get_element(node='login_succeed')
