import sys
import os

sys.path.append(os.getcwd())
from util.read_excel import Read_Excel
from base.actionMethod import ActionMethod


class Key_case(object):
    def __init__(self):
        self.RE = Read_Excel('E:\LX_selenium\config\key_case.xls')
        self.AM = ActionMethod()

    def run(self):
        # 获取行数
        nrows = self.RE.get_nrows()
        # 判断行数不为None执行用例
        if nrows:
            for i in range(1, nrows):
                # 获取是否运行用例值
                run_value = self.RE.get_cell_value(i, 3)
                # 判断用例运行值为运行则运行用例
                if run_value == 'yes':
                    method = self.RE.get_cell_value(i, 4)
                    handel_value = self.RE.get_cell_value(i, 5)
                    send_value = self.RE.get_cell_value(i, 6)
                    except_value_method= self.RE.get_cell_value(i,7)
                    except_value = self.RE.get_cell_value(i,8)
                    self.run_method(method=method, handel_value=handel_value, send_value=send_value)
                    #判断预期结果是否为空
                    if except_value != '':
                        except_value_list = self.RE.get_except_value(except_value)
                        if except_value_list[0] == 'text':
                            result = self.run_method(except_value_method)
                            if except_value_list[1] in result:
                                self.RE.write_value(i,9,'pass')
                            else:
                                self.RE.write_value(i,9,'fail')
                        elif except_value_list[0] == 'element':
                            result = self.run_method(except_value_method,except_value_list[1])
                            if result:
                                self.RE.write_value(i,9,'pass')
                            else:
                                self.RE.write_value(i,9,'fail')
                        else:
                            print('预期结果错误,只支持text/element')
                    else:
                        pass




    def run_method(self, method, handel_value=None, send_value=None):
        '''使用映射方法通过字符串找到类里的方法'''
        run_method = getattr(self.AM, method)

        if handel_value == '' and send_value == '':
            result = run_method()
        elif handel_value == '' and send_value != '':
            result = run_method(send_value)
        elif handel_value != '' and send_value == '':
            result = run_method(handel_value)
        else:
            result = run_method(handel_value, send_value)
        return result


if __name__ == '__main__':
    run = Key_case()
    run.run()
