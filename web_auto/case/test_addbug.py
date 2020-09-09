# coding:utf-8

import unittest

from selenium import webdriver

from web_auto.pages.add_bug import ZenTaoBug


class TestAddBug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.bug = ZenTaoBug(cls.driver)
        cls.bug.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def  test_add_bug(self):
        title = "接口报错1234567801"
        self.bug.add_bug(title)
        result = self.bug.is_add_bug_sucess(title)
        print(result)
        self.assertTrue(result)


if __name__ =="__main__":
    unittest.main()




