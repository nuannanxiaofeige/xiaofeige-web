# coding:utf-8
from selenium import webdriver
from web_auto.common.base import Base
import time

class ZenTaoBug(Base):  #继承


    # 定位登录
    loc_user = ("xpath","//*[@id='account']")
    loc_psw = ("xpath","//*[@name='password']")
    loc_com =("xpath","//*[@id='submit']")

    # 定位添加bug
    test_loc =("xpath","//*[@data-id='qa']") #点击测试
    bug_loc =("xpath","//*[@data-id='bug']") #点击BUG
    add_bug_loc =("xpath","//*[@id='createActionMenu']/a") #点击提bug
    trunk_loc = ("xpath","//*[@class='chosen-choices']")  #点击影响版本
    add_trunk_loc =("xpath","//*[@id='openedBuild_chosen']/div/ul/li")  #点击trunk
    input_title_loc =("xpath","//*[@id='title']")  #点击标题
    #需要先切换
    input_body_loc = ("xpath","//*[@class ='article-content']") #正文
    save_loc = ("xpath","//*[@id='submit']") #提交

    #新增列表
    new_bug_loc = ("xpath","//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    def login(self,user ="admin",psw ="123456"):
        self.driver.get("http://127.0.0.1:81/zentao/user-login.html")
        self.sendKeys(self.loc_user, user)
        self.sendKeys(self.loc_psw,psw)
        self.click(self.loc_com)

    def add_bug(self,title = "接口报错1234567801"):
        self.click(self.test_loc)
        self.click(self.bug_loc)
        self.click(self.add_bug_loc)
        self.click(self.trunk_loc)
        self.click(self.add_trunk_loc)

        self.sendKeys(self.input_title_loc,title)
        self.driver.switch_to.frame(0)   #切换iframe
        self.clear(self.input_body_loc)

        body = '''[前提条件]：在抽奖页面
        [执行步骤]：点击开始
        [实际结果]：轮盘没有转动
        [期望结果]：轮盘转动
        '''
        self.sendKeys(self.input_body_loc,body)
        self.driver.switch_to_default_content()  #切出iframe
        self.click(self.save_loc)

    def is_add_bug_sucess(self, _text):   #判断title是否正确
        return  self.is_text_in_element(self.new_bug_loc, _text)

if __name__=="__main__":
    driver=webdriver.Chrome()
    zentao = ZenTaoBug(driver)
    zentao.login()
    timestr =time.strftime("%Y_%m_%d_%H_%M_%S")
    title ="接口报错123"+timestr
    zentao.add_bug(title)
    result = zentao.is_add_bug_sucess(title)
    print(result)
