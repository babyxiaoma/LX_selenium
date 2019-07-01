import logging
import os
import datetime


class Logs(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        #获取当前路径的目录组件
        base_file = os.path.dirname(os.path.abspath(__file__))
        #拼接路径名
        log_dir = os.path.join(base_file, 'logs')
        #获取以年月日格式以.log为后缀的str
        log_file = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
        #拼接路径和当前时间为名字的路径名
        log_name = log_dir+'\\'+str(log_file)


        self.file_handle = logging.FileHandler(log_name,'a',encoding='GBK')
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s -- %(filename)s -- %(funcName)s -- %(lineno)d --%(levelname)s -- %(levelno)s --- %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)


    def user_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == '__main__':
    log = Logs()
    log.user_log()
    log.logger.debug('the is a debug msg')
    log.close_handle()