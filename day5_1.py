# author:jason
'''
    任务1：
        将导航系统与商城系统结合一起。
'''
def shopping():

    import random
    # 货架
    shop=[
        ["平板",1000],
        ["笔记本",2000],
        ["手机",500],
        ["水杯",20]
    ]
    # 抽取优惠卷
    juan = random.randint(0,1)
    while True:
        chou = input("是否抽取优惠卷y/n：")
        if chou == "y":
            if juan == 0:
                print("恭喜抽中平板1折劵")
            elif juan == 1 :
                print ("恭喜抽中笔记本7折劵")
            break
        elif chou == "n":
            break
        else :
            print("请重新输入：")

    # 初始化余额
    money=input("请输入余额：")
    money=int(money)

    # 购物车清零
    che=[]

    # 购买商品
    while True:
        #打印商品货架
        for hao , ming in enumerate(shop):
            print (hao,ming)
        #购买商品
        xuan = input("请选择你购买的商品：")
        print(xuan)
        if  xuan.isdigit(): #判断是否为数字

            xuan=int(xuan) #如果购买不存在的商品
            if xuan > 3:
                print("商品不存在，请重新输入：")
            else :
                if chou == "y":
                    #购买打折扣的商品
                    if juan == 0 and xuan == 0 and money >= shop[xuan][1]*0.1:
                        che.append(shop[xuan])  #加入购物车
                        money = money - shop[xuan][1]*0.1  #计算余额
                        print ("恭喜您，加入购物车成功，您的余额为：",money)
                    elif juan == 1 and xuan == 1 and money >= shop[xuan][1]*0.7:
                        che.append(shop[xuan])  #加入购物车
                        money = money - shop[xuan][1]* 0.7  #计算余额
                        print("恭喜您，加入购物车成功，您的余额为",money)

                    #购买未打折扣的商品
                    elif money >= shop[xuan][1]:
                        che.append(shop[xuan])  #加入购物车
                        money = money - shop[xuan][1]   #计算余额
                        print("恭喜您，加入购物车成功，您的余额为：",money)

                    else : # 余额不足的情况下
                        print("余额不足，请购买其他商品")
                else:
                    if money >= shop[xuan][1]:
                        che.append(shop[xuan][1])   #加入购物车
                        money =money-shop[xuan][1]  #计算余额
                        print("恭喜您，加入购物车成功，您的余额为：",money)
                    else:
                        print("余额不足，请购买其他商品")

        #退出购物
        elif xuan == "q":
            break

        #输入错误
        else :
            print("输入错误，请重新输入：")

    #打印小票
    print("以下是您的购物小条，请拿好：")
    for ming , qian in enumerate(che,1):
        print(ming , qian)
    print("您的余额为",money)




data = {
    "北京":{
        "昌平":{
            "十三陵":["十三陵水库","沙河水库"],
            "高校":["北京邮电大学","中央戏剧学院","北京师范大学","华北电力大学","北京航空航天大学"],
            "天通苑":["海底捞","呷哺呷哺"]
        },
        "海淀":{
            "公主坟":["军事博物馆","中华世纪园"],
            "科普场馆":["中国科技馆","北京天文馆"],
            "高校":["北京大学","清华大学"],
            "景区":["北京植物园","香山公园","玉渊潭公园"]
        },
        "朝阳":{
            "龙城":["鸟化石国家地质公园","朝阳南北塔"],
            "双塔":["朝阳凌河公园","朝阳凤凰山"]
        },
        "延庆":{
            "龙庆峡":["龙庆峡景区"]
        }
    },
    "上海":{
        "浦东新区":{
            "上海科技馆":["动物世界","吸烟区","特展厅"],
            "世纪广场":["东方之光","上海东方艺术中心"],
        },
        "静安区":{
            "国立大厦":["东海广场","信达大厦"],
            "静安寺":["释迦摩尼佛","东厢房","观音殿"],
        },
    },
    "广州":{
        "白云区":{
            "丽景湾":["新纪元商贸大厦","广州雕塑公园"],
        },
        "花都区":{
            "石山岭":["海角","中围"],
        },
        "从化区":{
            "欣荣广场":["柳溪中学","美宜佳"]
        }
    }
}


# 打印城市
def print_place(choice):
    for i in choice:
        print(i)

# 攻略
for i in data:
    print(i)

while True:
    shu1=input("请输入您要去的城市（按q/Q退出）：")
    if shu1 in data:
        print_place(data[shu1])
        shu2 = input("请输入您要去的二级城市（按q/Q退出）：")


        if shu2 in data[shu1]:
            print_place(data[shu1][shu2])
            shu3 = input("请输入您要去的三级城市（按q/Q退出）：")


            if shu3 in data[shu1][shu2]:
                print("该地区有景点：")
                print_place(data[shu1][shu2][shu3])
                gou=input("请问是否需要购物：购物输入y，退出输入n")
                if gou == "y":
                    shopping()

                elif gou == "n":
                    print("退出购物成功！")
                    break

                else :
                    print("输入错误，请重新输入!")

            elif shu3 == "q" or shu3 == "Q":
                print("退出成功")
                break

            else:
                print("输入错误，请重新输入（按q/Q退出）")

        elif shu2 == "q" or shu2=="Q":
            print("退出成功！")
            break

        else:
            print("输入错误，请重新输入二级城市（按q/Q退出）：")

    elif shu1 == "q" or shu1 == "Q":
        print("退出成功！")
        break

    else:
        print("输入错误，请重新输入城市（按q/Q退出）：")
