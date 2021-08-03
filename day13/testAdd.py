'''
    单元测试：
        1.unittest单元组件
        1.1 继承TestCase测试用例
        1.2 测试用例方法命名必须是testXXXX
        1.3 使用assertEqual()来断言

'''
import unittest
from Calc import Calc
class TestCalc(unittest.TestCase):

    def testAdd(self):
        # 1.准备数据
        a = 6
        b = 5
        c = 11
        # 2.调用被测程序
        calc = Calc()
        sum = calc.add(a,b)

        # 3.断言
        self.assertEqual(c,sum)

    def testAdd1(self):
        # 1.准备数据
        a = -6
        b = -5
        c = -11
        # 2.调用被测程序
        calc = Calc()
        sum = calc.add(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testsubs(self):
        a = 20
        b = 10
        c = 10
        calc = Calc()
        cha = calc.subs(a, b)

        self.assertEqual(c, cha)

    def testsubs1(self):
        a = 89
        b = 12
        c = 77
        calc = Calc()
        cha = calc.subs(a, b)
        self.assertEqual(c,cha)

    def testmulti(self):
        a = 12
        b = 89
        c = 1068
        calc = Calc()
        ji = calc.multi(a,b)
        self.assertEqual(c , ji)

    def testdevision(self):
        a = 98
        b = 21
        c = 4
        calc = Calc()
        shang = calc.devision(a, b)
        self.assertEqual(c,shang)















