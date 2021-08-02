'''
    厨师：一共有3个厨师同时造面包，面包0.5s造一个
    顾客：一共有5个顾客，每个顾客有3000元，同时去抢面包
    篮子：最多可以容纳3000个面包，每个面包2元
'''
from threading import  Thread
lanzi = 0 #篮子
import time
class shangdian(Thread):
    chushi = ""
    def run(self) -> None:
        global lanzi
        while True:
            if lanzi <200:
                lanzi = lanzi + 1
                time.sleep(0.5)
                print(self.chushi,"已经造了一个面包，现在篮子里有",lanzi,"个面包")
            elif lanzi == 200:
                break

class shopping(Thread):
    username = ""
    count = 0
    def run(self) -> None:
        global lanzi
        while True :
            if lanzi >199:
                lanzi = lanzi - 1
                self.count = self.count+1
                time.sleep(0.005)
                print(self.username,"抢了一个面包，现在还剩",lanzi,"个面包")
            elif lanzi <=0:
                break



s1 = shangdian()
s2 = shangdian()
s3 = shangdian()

a1 = shopping()
a2 = shopping()
a3 = shopping()
a4 = shopping()
a5 = shopping()

#定义厨师
s1.chushi = "蔡徐坤"
s2.chushi = "罗志祥"
s3.chushi = "吴亦凡"

#定义顾客
a1.username = "甲"
a2.username = "乙"
a3.username = "丙"
a4.username = "丁"
a5.username = "卯"
#运行
s1.start()
s2.start()
s3.start()

a1.start()
a2.start()
a3.start()
a4.start()
a5.start()











