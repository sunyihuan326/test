# coding:utf-8
'''
Created on 2016/9/20

@author: sunyihuan
'''

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://yanzijia.cn")


browser.quit()
