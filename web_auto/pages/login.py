# coding:utf-8
from selenium import webdriver
from web_auto.common.base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url ="http://127.0.0.1:81/zentao/user-login.html"

class Login(Base):

    # 定位登录
    loc_user = ("xpath","//*[@id='account']")
    loc_psw = ("xpath","//*[@name='password']")
    loc_button =("xpath","//*[@id='submit']")
    loc_keep = ("id","keepLoginon")
    loc_forget_psw =("link text","忘记密码")
    loc_get_userinfo = ("id","userMenu")
    loc_refresh = ("link text","刷新")



    def input_user(self,text):   #输入账号
        self.sendKeys(self.loc_user,text)

    def input_psw(self,text):    #输入密码
        self.sendKeys(self.loc_psw,text)

    def click_keep_login(self):     #点击‘保持登录’按钮
        self.click(self.loc_keep)

    def click_forget_psw(self):    #点击‘忘记密码’按钮
        self.click(self.loc_forget_psw)

    def click_button(self):    #点击‘登录’按钮
        self.click(self.loc_button)

    def get_username(self):  #获取用户信息
        user =  self.get_text(self.loc_get_userinfo)
        return user

    def get_login_result(self,user):
        result = self.is_text_in_element(self.loc_get_userinfo,user)
        return result

    def get_refresh_exist(self):
        '''判断忘记密码页，刷新按钮是否存在'''
        a = self.findElementNew(self.loc_refresh)
        return a


    def is_alert_exist(self): #判断alert是不是在，返回text或者False
        a = self.is_alert()
        if a:
            print(a.text)
            a.accept()


    def login(self,user ="admin",psw ="123456",keep_login=True):  #如果为False，则不点击保存登录
        self.driver.get (url)
        self.input_user(user)
        self.input_psw(psw)
        if keep_login : self.click_keep_login( )
        self.click_button()


if __name__ =="__main__":
    driver = webdriver.Chrome()
    driver.get(url)
    login = Login(driver)
    login.login()

    # login.input_user(text="admin")
    # login.input_psw(text="123456")
    # login.click_keep_login()
    # login.click_forget_psw()
    # # login.click_button()

