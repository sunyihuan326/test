# coding:utf-8
'''
Created on 2016/9/20

@author: sunyihuan
'''

from selenium import webdriver

browser = webdriver.Ie()

# "浏览器最大化"
# browser.maximize_window()

# 设置浏览器宽高
# browser.set_window_size(600, 800)

url = "http://devsheji.yanzijia.cn/m/login"
browser.get(url)

browser.find_element_by_id('account').send_keys("lby")
browser.find_element_by_id("password").send_keys("123456")
browser.find_element_by_id("J-login-btn").click()


# browser.refresh()
browser.quit()
