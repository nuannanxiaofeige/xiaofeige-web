# coding:utf-8

from selenium import webdriver
import unittest,ddt
from web_auto.pages.login import Login,url
from web_auto.common.read_excel import ExcelUitl
import os


'''
1、输入admin，输入123456，点击登录
2、输入admin，输入  ，点击登录
3、输入admin，输入12345，点击登录
4、输入admin,输入123456，点击保持登录，点击登录
'''


# 测试数据
testdates =[
        {"user":"admin","psw":"123456","expect": True},
        {"user":"admin","psw":" ","expect": False},
        {"user":"admin","psw":"12345","expect": False}
           ]

# #获取excel
# propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) #获取当前脚本的路径
# filepath = os.path.join(propath,"common","data.xls")
# print(filepath)
# data = ExcelUitl(filepath)
# testdates = data.dict_data()
# print(testdates)

@ddt.ddt
class TestLogin(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.login_pag = Login(cls.driver)

    def setUp(self):
        self.driver.get(url)
        self.login_pag.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def login_case(self,user,psw,expect):
        self.login_pag.login(user,psw)
        result = self.login_pag.get_login_result(user)
        if expect =="True": expect_result = True  #字符串改成bool值
        else:expect_result = False
        print("测试结果：%s"% result)
        self.assertTrue(result == expect)



    @ddt.data(*testdates)
    def test_01(self, data):
        print("------------开始测试-----------")
        print("测试数据: %s" % data)
        self.login_case(data["user"], data["psw"], data["expect"])
        print("--------------测试结束-------------")



    def test_04(self):
        '''输入admin,输入123456，点击保持登录，点击登录'''
        print("------------开始测试: test04-----------")
        data4 = testdates[0]
        print("测试数据：%s"%data4)
        self.login_pag.click_keep_login()
        self.login_case(data4["user"],data4["psw"],data4["expect"])
        print("--------------测试结束-------------")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ =="__main__":
    unittest.main()
