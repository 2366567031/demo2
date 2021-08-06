from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from ICBCBank import Bank
'''
    DDT:data driver test
        ddt
        data
        unpack
    1.测试类必须用@ddt修饰
    2.测试方法使用@data引入数据源
    任务：
        将工行系统的核心业务进行测试？
        bank_addUser()

'''
# 数据源
# 数据源
add = [
    [1,1,123456,1,1,1,1,1111,None],
    [2,"小李",123456,"中国","河南","jd","门派",3000,None]
]
da = [
    [1, 100],

]
draw = [
    [1,123456,100],

]

transfer = [
    [1, 123456,2, 1]
]

query = [
    [1,123456],

]


@ddt  # 注解，注释这个类是参数化类
class TestCalc(TestCase):
    @data(*add)  # 引入数据源
    @unpack
    def testbank_addUser(self,account, username, password, country, province, street, gate, money, registerDate):
        # 2.调用被测方法
        bank = Bank()
        bank.bank_addUser(account, username, password, country, province, street, gate, money, registerDate)
        # 3.断言

    @data(*da)  # 引入数据源
    @unpack
    def testbank_saveMoney(self, account1, savemoney1):
        # 2.调用被测方法
        bank = Bank()
        bank.bank_saveMoney(account1, savemoney1)
        # 3.断言

    @data(*draw)  # 引入数据源
    @unpack
    def testbank_drawMoney(self, account, password, draw):
        # 2.调用被测方法
        bank = Bank()
        bank.bank_drawMoney(account, password, draw)
        # 3.断言

    @data(*transfer)  # 引入数据源
    @unpack
    def testbank_transfer(self,account, password, transfer_account, transfer_money):
        # 2.调用被测方法
        bank = Bank()
        bank.bank_transferMoney(account, password, transfer_account, transfer_money)
        # 3.断言

    @data(*query)  # 引入数据源
    @unpack
    def testbank_query(self, account, password):
        # 2.调用被测方法
        bank = Bank()
        bank.bank_userQuery(account, password)
        # 3.断言





















