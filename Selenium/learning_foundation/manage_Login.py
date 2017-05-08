# coding:utf-8
'''
Created on 2016/9/20

@author: sunyihuan
'''

from selenium import webdriver

browser = webdriver.Ie()

# browser=webdriver.PhantomJS()
# "浏览器最大化"
# browser.maximize_window()

# 设置浏览器宽高
# browser.set_window_size(600, 800)

url = "http://sheji.yanzijia.cn/m/login"
browser.get(url)

# 登录页面
browser.find_element_by_id('account').clear()
browser.find_element_by_id('account').send_keys("lby")
browser.find_element_by_id("password").clear()
browser.find_element_by_id("password").send_keys("123456")
browser.find_element_by_id("J-login-btn").click()

# 进入主页素材页面
browser.find_element_by_link_text('主页素材').click()
# 进入数据分析页面
browser.find_element_by_link_text('数据分析').click()
# 进入流量统计页面
browser.find_element_by_link_text('流量统计').click()



# 浏览器刷新
browser.refresh()


browser.quit()       # 退出