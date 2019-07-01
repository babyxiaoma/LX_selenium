from page.login_page import Login_Page

class Login_Dandle(object):
    def __init__(self,driver=None):
        self.LP = Login_Page(driver=driver)

    def send_username(self,username):
        '''输入用户名'''
        self.LP.get_username_element().send_keys(username)

    def send_password(self,password):
        '''输入密码'''
        self.LP.get_password_element().send_keys(password)

    def click_button(self):
        '''点击登录按钮'''
        self.LP.get_login_button_element().click()

    def error_click_button(self):
        '''点击错误提示框按钮'''
        self.LP.get_error_button_element().click()

    def get_login_succeed_text(self):
        '''获取登录界面信息'''
        return self.LP.get_login_succeed_element()


    #此处用这样文本判断有问题
    def user_info_text(self,info,user_info):
        '''获取登录成功失败文本信息'''
        try:
            if info == 'username_error':
                text = self.LP.get_username_element().text
            else:
                text = self.LP.get_password_element().text
        except:
            text = None
        return text



