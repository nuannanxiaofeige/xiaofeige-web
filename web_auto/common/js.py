from selenium import webdriver
import time
from web_auto.common.base import Base




driver= webdriver.Chrome()
driver.get ("https://www.cnblogs.com/yoyoketang/?_wv=1031")


time.sleep(3)

#滑动到底部
js_heig = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js_heig)

#滑动到顶部
js_top ="window.scrollTo(0,0)"
driver.execute_script(js_top)

#滑动到指定元素那里
loc1 = driver.find_element_by_link_text("pytest文档45-allure添加环境配置(environment)")
driver.execute_script("arguments[0].scrollIntoView();",loc1)


# js定位iframe
driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby9idWctY3JlYXRlLTEtMC1tb2R1bGVJRD0wLmh0bWw=.html")
# jS操作快，需要先sleep
time.sleep(2)
body ="hello"
js = "document.getElementsByClassName('ke-edit-iframe')[0].contentWindow.document.body.innerHTML = body"



# # js定位元素(非iframe)
# driver.get ("")
# time.sleep(3)
# body ="hello"
# js = "document.getElementById("").value= body"
# driver.execute_script(js)
