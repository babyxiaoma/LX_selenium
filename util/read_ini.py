import configparser

class Config_Ini(object):
    def __init__(self,file_name='E:/LX_selenium/config/config.ini',key='user_element'):
        if file_name and key:
            self.file_name = file_name
            self.key = key
        self.cf = configparser.ConfigParser()


    def get_element(self,node):
        self.cf.read(self.file_name)
        data = self.cf.get(self.key,node)
        return data





if __name__ == '__main__':
    cfg = Config_Ini()
    print(cfg.get_element(node='username'))



