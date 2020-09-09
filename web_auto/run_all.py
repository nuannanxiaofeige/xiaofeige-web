# coding:utf-8
import unittest
import time
import os
import sys
import HTMLTestRunner_cn


current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

# 用例路径
casePath = "H:\PythonWorkSpace.3\web_auto\case"

rule = "test*.py"

discover = unittest.defaultTestLoader.discover(start_dir = casePath , pattern=rule)
print  (discover)


# 报告路径
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
reportPath = "H:\\PythonWorkSpace.3\\web_auto\\report\\"+"report"+now+".html"

fp = open(reportPath,"wb")
runner  = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                          title="测试用户登陆",
                                          description="描述")
                                          # retrue = 1)#失败重跑一次

runner.run(discover)

# fp.close()