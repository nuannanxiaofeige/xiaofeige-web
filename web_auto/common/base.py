# coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Base():
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.timeout = 30
        self.t = 0.5

    def findElement(self,locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id","valuel")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*locator))
            return  ele


    '''定位到元素返回元素对象，未定位到返回TimeOut异常'''
    def findElementNew(self,locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id","valuel")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
            return ele


    def sendKeys(self,locator,text):
        a = self.findElement(locator)
        a.send_keys(text)

    def click(self,locator):
        a = self.findElement(locator)
        a.click()

    def clear(self,locator):
        a = self.findElement(locator)
        a.clear()

    def isSelected(self,locator):
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r


    def is_alert(self):
        '''判断页面上是否有alert'''
        try:
            result = WebDriverWait(self.driver,self.timeout ,self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def is_alert_exist(self):
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except:
            return False

    def is_tilte(self,_tilte):
        '''获取title'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(_tilte))
            return result
        except:
            return False

    def is_text_in_element(self,locator,text=""):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id","valuel")')
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,text))
            return result
        except:
            return False


    def get_text(self,locator):
        '''获取文本'''
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("获取文本失败，返回' '")
            return " "

    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        ele = self.findElementNew(locator)
        ActionChains(self.driver).move_to_element(ele).perform()


    '''select方法封装'''
    def select_by_index(self,locator,index=0):
        '''通过索引，index是索引第几个，从0开始，默认选第一个'''
        ele = self.findElement(locator)
        Select(ele).select_by_index(index)

    def select_by_value(self,locator,value):
        '''通过value属性'''
        ele = self.findElement(locator)
        Select(ele).select_by_value(value)

    def select_by_text(self,locator,text):
        '''通过文本定位'''
        ele = self.findElement(locator)
        Select(ele).select_by_visible_text(text)

    def js_scroll_end(self , x = 0):   # 横向滚动: y
        '''滑动到底部'''
        self.js_he = "window.scrollTo(%s,document.body.scrollHeight)"%x
        self.driver.execute_script(self.js_he)

    def js_scroll_top(self):
        '''滑动到顶部'''
        self.js_top = "window.scrollTo(0,0)"
        self.driver.execute_script(self.js_top)

    def js_focus(self,locator):
        '''滑动到页面上某个元素'''
        ele = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)





if __name__ =="__main__":
    driver= webdriver.Chrome()
    driver.get("https://finance-test.hdl100.cn/#/login")
    CW =Base(driver)
    loc1 = ("xpath","//input[@placeholder='请输入用户名']")
    loc2 = ("xpath","//input[@placeholder='请输入密码']")
    loc3 = ("xpath","//*[@type='button']")

    CW.sendKeys(loc1,"supperadmin")
    CW.sendKeys(loc2,"123456")
    CW.click(loc3)




