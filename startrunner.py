import time ,sys
sys.path.append('../')
import unittest,os
from base.HTMLTestRunner import HTMLTestRunner
from suit.testsuit import testsuit
report_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class YoungMKTestRunner(object):
    def run_tests(self):
        # 创建一个测试套件
        allsuit = unittest.TestSuite()
        # 在测试套件中添加需要运行的测试用例
        aa = testsuit(allsuit).add_testSuit()
        self.filename = report_path + "\\report\\" + time.strftime("%Y-%m-%d %H_%M_%S") + "result.html" # 测试结果存储路径
        path = open(self.filename, "wb")  # 自动生成测试报告
        runner = HTMLTestRunner(stream=path,
                                verbosity=2,
                                title="登录测试结果",
                                description="用例执行结果:",
                                retry=1)  # 测试用例编辑
        print("测试报告路径：%s" %self.filename)
        runner.run(aa)  # 执行测试用例
        path.close()  # 关闭测试报告

if __name__ == "__main__":
     start = YoungMKTestRunner()
     start.run_tests()
     print("测试结束")
     print("第二次提交")

