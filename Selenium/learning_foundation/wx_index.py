# coding:utf-8
'''
Created on 2017/5/8

@author: sunyihuan
'''
from selenium import webdriver


browser = webdriver.Ie()
url="http://sheji.yanzijia.cn/wx/index#"

browser.get(url)
browser.find_element_by_link_text('免费推荐').click()

browser.quit()

