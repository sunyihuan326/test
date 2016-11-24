# coding:utf-8
'''
Created on 2016/10/26

@author: sunyihuan
'''
from Widget import Widget

import unittest


class WidgetTestCase(unittest.TestCase):
    def runTest(self):
        widget = Widget()
        self.assertEqual(widget.getSize(), (40, 40))


if __name__ == "__main__":
    testCase = WidgetTestCase()
    testCase.runTest()
