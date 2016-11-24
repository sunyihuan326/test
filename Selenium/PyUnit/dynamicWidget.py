# coding:utf-8
'''
Created on 2016/10/26

@author: sunyihuan
'''
import Widget
import unittest


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget.Widget()

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))

    def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))


if __name__ == "__main__":
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(WidgetTestCase("testSize"))
    # suite.addTest(WidgetTestCase("testResize"))
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

