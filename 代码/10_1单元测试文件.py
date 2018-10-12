'''
开始测试
1.导入单元测试的模块unittest
2.创建测试类，这个类必须继承自unittest.TestCase
'''
import unittest
from 单元测试 import mySum
from 单元测试 import mySub

class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试时自动调用")
    def tearDown(self):
        print("结束测试时自动调用")
    # 测试mySum函数
    def test_mySum(self):
        self.assertEqual(mySum(10,20),30,"加法有误")
    # 测试mySub函数
    def test_mySub(self):
        self.assertEqual(mySub(20,10),10,"减法有误")

if __name__=="__main__":
    unittest.main()