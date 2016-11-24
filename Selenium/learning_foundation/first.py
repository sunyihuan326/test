# coding:utf-8
'''
Created on 2016/9/20

@author: sunyihuan
'''

from selenium import webdriver

browser = webdriver.Ie()


# browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element_by_id('kw').send_keys("selenium")
browser.find_element_by_id("su").click()

# browser.refresh()
browser.quit()
