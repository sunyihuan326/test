# coding:utf-8
'''
Created on 2016/11/2

@author: sunyihuan
'''
from appium import webdriver
#
# def f(x,y):
#     z=x+y
#     return z
# print f(1,3)

# -*- coding:utf-8 -*-
# 用python实现排列组合C(n,m) = n!/m!*(n-m)!
def get_value(n):
    if n==1:
        return n
    else:
        return n * get_value(n-1)

def gen_last_value(n,m):
     first = get_value(n)
     print "n:%s     value:%s"%(n, first)
     second = get_value(m)
     print "n:%s     value:%s"%(m, second)
     third = get_value((n-m))
     print "n:%s     value:%s"%((n-m), third)
     return first/(second * third)


if __name__ == "__main__":
    # C(12,5)
    rest = gen_last_value(15,5)
    print "value:", rest


print 15*14*13*12*11/(5*4*3*2)