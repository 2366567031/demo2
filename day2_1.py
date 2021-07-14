'''
    变量：
        可以变化存储数据的量。
    定义:
        规则：
        26个英文字母大小写：52
        0~9 ： 10个
        _ : 特殊字符
        总共：63个
    规范：
        数字不能开头
        不能使用python的关键字

        升级：
            将产物的所有信息全部 用变量存储

'''
# 1.存储第一个商品
id1 = 1
name1 = "羽绒服"
price1 = 25.5
num1 = 500
sale1 = 10
quan1 = "A+"
add1 = "新疆"

# 2.存储第一个商品
id2 = 2
name2 = "风衣"
price2 = 360
num2 = 500
sale2 = 50
quan2 = "A+"
add2 = "山东"

# 3.存储第一个商品
id3 = 3
name3 = "丁字裤"
price3 = 265
num3 = 600
sale3 = 121
quan3 = "B+"
add3 = "海南"


print("---------------------------------Jason商城系统-----------------------------------")
print("--------------------------------------------------------------------------------")
print("编号      名称       单价      库存数量        今日销售数量         质量        产地")
print("--------------------------------------------------------------------------------")
print(id1,"     ",name1,"       ",price1,"          ",num1,"      ",sale1,"      ",quan1,"           ",add1)
print(id2,"     ",name2,"       ",price2,"          ",num2,"      ",sale2,"      ",quan2,"           ",add2)
print(id3,"     ",name3,"       ",price3,"          ",num3,"      ",sale3,"      ",quan3,"           ",add3)
print("-----------------------------------------------------------------------------------")
print("总销售额：￥",(price1 * sale1 + price2 * sale2 + price3 * sale3))


char=1
print(char)

# Cy%ty=1
# print(Cy%ty)  错误

Oax_li=1
print(Oax_li)

# $123=1
# print($123)   错误

flul=1
print(flul)

# 3_3=1
# print(3_3)

BYTE=1
print(BYTE)

T_T=1
print(T_T)

# 有以下两个数，使用+，-号实现两个数的调换。
a=56
b=78
a=a+b
b=a-b
a=a-b
print(a,b)

# 定义两个变量stu1和stu2，分别存储45和23，并用print()打印两个数的和
stu1=45
stu2=23
print(stu1+stu2)

# 定义5个变量，并用print()打印5个数的和、平均值
num1=5
num2=4
num3=1
num4=4
num5=1
print('和：',num1+num2+num3+num4+num5,'平均值：',(num1+num2+num3+num4+num5)/5)

# 定义一个变量num1,并赋值45.然后将num1值赋值给num2。打印出来
num1=45
num2=num1
print(num2)


















