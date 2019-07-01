from handle.login_handle import Login_Dandle
import time

class Login_Business(object):
    def __init__(self,driver):
        self.LD = Login_Dandle(driver=driver)

    def login(self,username,password):
        '''执行操作'''
        self.LD.send_username(username=username)
        self.LD.send_password(password=password)
        self.LD.click_button()


    def login_succeed(self,username,password):
        '''登录成功'''
        self.login(username=username,password=password)
        time.sleep(2)
        if self.LD.get_login_succeed_text() == None:
            return True
        else:
            return False

    def login_username_error(self,username,password):
        '''用户名错误'''
        self.login(username=username,password=password)
        time.sleep(2)
        self.LD.error_click_button()
        if self.LD.user_info_text('username_error','用户名或密码错误') == None:
            return True
        else:
            return False

    def login_password_error(self,username,password):
        '''密码错误'''
        self.login(username=username,password=password)
        time.sleep(2)
        self.LD.error_click_button()
        if self.LD.user_info_text('password_error','用户名或密码错误') == None:
            return True
        else:
            return False



    #使用ddt数据驱动
    def register_function(self,username,password,assertCode,assertText):
        self.login(username=username,password=password)
        time.sleep(2)
        if self.LD.user_info_text(assertCode,assertText) == None:
            return True
        else:
            return False




