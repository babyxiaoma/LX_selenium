import HTMLTestRunner
import os
import unittest


def run():
    '''运行测试用例生成html报告'''
    file_path = os.path.join(os.getcwd() + r'\case1.html')
    print(file_path)
    case_path = os.path.join(os.getcwd())
    print(case_path)
    with open(file_path, 'wb') as f:
        suite = unittest.defaultTestLoader.discover(start_dir=case_path, pattern='first_*.py')

        runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                               verbosity=2,
                                               title='web自动化测试报告',
                                               description='这是第一次的测试报告')
        runner.run(suite)

run()