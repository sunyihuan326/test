# coding:utf-8
'''
Created on 2017/1/4

@author: sunyihuan
'''
import xlwt



xls_header = ['代理ID', '姓名', '手机', '月份', '结算金额', '销售额', '结算状态', '操作时间', '备注']
xls = xlwt.Workbook(encoding='utf-8')
table_1 = xls.add_sheet("未结算")
table_2 = xls.add_sheet("已结算")
for k, v in enumerate(xls_header):
    table_1.write(0, k, v)
    table_2.write(0, k, v)
xls.save('1.xls')