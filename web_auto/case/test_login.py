# coding:utf-8

from selenium import webdriver
import unittest
from web_auto.pages.login import Login,url
import  ddt




'''
1、输入admin，输入123456，点击登录
2、输入admin，输入  ，点击登录
3、输入admin，输入12345，点击登录
4、输入admin,输入123456，点击保持登录，点击登录
5、点击忘记密码
'''

class Test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.login_pag = Login(cls.driver)

    def setUp(self):
        self.driver.get(url)
        self.login_pag.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()


    def test_01(self):
        '''输入admin，输入123456，点击登录'''
        self.login_pag.input_user("admin")
        self.login_pag.input_psw("123456")
        self.login_pag.click_button()
        result = self.login_pag.get_username()
        self.assertTrue(result =="admin")

    def test_02(self):
        '''输入admin，输入  ，点击登录'''
        self.login_pag.input_user("admin")
        self.login_pag.click_button()
        result = self.login_pag.get_username()
        self.assertTrue(result == " ")

    def test_03(self):
        '''输入admin，输入12345，点击登录'''
        self.login_pag.input_user("admin")
        self.login_pag.input_psw("12345")
        self.login_pag.click_button()
        result = self.login_pag.get_username()
        self.assertTrue(result == " ")

    def test_04(self):
        '''输入admin,输入123456，点击保持登录，点击登录'''
        self.login_pag.input_user("admin")
        self.login_pag.input_psw("123456")
        self.login_pag.click_keep_login()
        self.login_pag.click_button()
        result = self.login_pag.get_username()
        self.assertTrue(result =="admin")

    def test_05(self):
        '''点击忘记密码'''
        self.login_pag.click_forget_psw()
        result = self.login_pag.get_refresh_exist()
        self.assertTrue(result)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    # def test_02(self):

if __name__ =="__main__":
    unittest.main()
