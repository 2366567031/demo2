# class Shuibei:
#     __name = ""
#     __gaodu = 0
#     __rongji = 0
#     __yanse = ""
#     __caizhi = ""
#
#     def setname(self,name):
#         self.__name = name
#
#     def getname(self):
#         return self.__name
#
#     def setgaodu(self,gaodu):
#         if gaodu > 20 :
#             print("高度过高，请重新输入！")
#         else :
#             self.__gaodu = gaodu
#
#     # def getgaodu(self):
#     #     return self.__gaodu
#
#     def setrongji(self,rongji):
#         if rongji > 20 :
#             print("容积过大，请重新输入！")
#         else:
#             self.__rongji = rongji
#
#     def rongji(self,rongji):
#         print(self.__name,"的容积为",rongji)
#
#     # def getrongji(self):
#     #     return self.__rongji
#
#     def setyanse(self,yanse):
#         self.__yanse = yanse
#
#     # def getyanse(self):
#     #     return self.__yanse
#
#     def setcaizhi(self,caizhi):
#         self.__caizhi = caizhi
#
#     # def getcaizhi(self):
#     #     return self.__caizhi
#
#     def gaodu(self,gaodu):
#         print("水杯的高度为",gaodu)
#
#
#     def beizi(self):
#         print("水杯的高度为：",self.__gaodu,",容积为：",self.__rongji,"水杯的颜色是，",self.__caizhi,"水杯的材质是，",self.__caizhi)
#
#     def zuoyong(self):
#         print("这个水杯可以存放",self.__rongji,"ml","的液体")
#
# s=Shuibei()
# s.setname ("富广")
# #水杯的高度
#
# s.setgaodu  (10)
# #水杯的容积
# s.setrongji (10)
# #水杯的颜色
# s.setyanse("红色")
# #水杯的材质
# s.setcaizhi("塑料")
#
#
# print(s.getname())
#



class shuibei:
    __name = ""
    __rongji = 0
    __gaodu =  0

    def setname(self,name):
        self.__name = name

    def getname(self):
        return self.__name

    def setrongji(self,rongji):
        if rongji >= 20 :
            print("容积过大，重新输入！")
        else:
            self.__rongji = rongji

    def setgaodu(self,gaodu):
        self.__gaodu =   gaodu

    def weizhi(self,weizhi):
        print(self.__name,"放在",weizhi)

    def zhuren(self,zhuren):
        print(self.__name,"的主人是",zhuren)

s=shuibei()

s.setname("富广水杯")
s.setgaodu(20)
s.setrongji(10)

s.weizhi("桌子上")
s.zhuren("车志阳")




class diannao :
    __pingmu = 0
    __jiage = 0
    __cup = ""
    __neicun = 0
    __daiji = 0

    def setpingmu(self,pingmu):
        self.__pingmu = pingmu

    def getpingmu(self):
        return self.__pingmu

    def setjiage(self,jiage):
        self.__jiage = jiage

    def getjiage(self):
        return self.__jiage

    def setcpu(self,cpu):
        self.__cpu = cpu

    def getcpu(self):
        return self.__cpu

    def setneicun(self,neicun):
        self.__neicun = neicun

    def getneicun(self):
        return self.__neicun

    def setdaiji(self,daiji):
        self.__daiji = daiji

    def getdaiji(self):
        return self.__daiji

    def dazi(self,dazi):
        print("这个电脑可以",dazi)

    def youxi(self,youxi):
        print("这个电脑可以玩",youxi)

    def shipin(self,shipin):
        print("这个电脑可以看",shipin)


d=diannao()

d.setpingmu(20)
d.setjiage(5000)
d.setcpu("因特")
d.setneicun(16)
d.setdaiji(20)

d.dazi("打字")
d.youxi("英雄联盟")
d.shipin("小视频")













