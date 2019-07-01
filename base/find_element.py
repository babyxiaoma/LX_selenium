# from util.read_ini import Config_Ini
from log.log import Logs

class Driver_Emelent(object):
    def __init__(self, driver):
        get_Log = Logs()
        self.logger = get_Log.user_log()
        self.driver = driver
        #此实例化获取数据时可以传不同文件路径和key名
        # self.config = Config_Ini()

    def get_element(self,node):
        #使用关键字模型改变在excel上面写定位节点
        # data = self.config.get_element(node=node)
        by = node.split('>')[0]
        value = node.split('>')[1]
        self.logger.info('定位方式:' + by + '--->定位值为:' + value)
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'class':
                return self.driver.find_element_by_class_name(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            else:
                return self.driver.find_element_by_link_text(value)
        except:
            return None
