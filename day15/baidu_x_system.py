
'''
    w:写入
    r:读取
    +: r+ w+
    a:附加
    b:byte  wb  rb
'''
# 获取文件句柄
# f = open(file="data.txt",mode="r+",encoding="utf-8")

# 读取文件信息
# data = f.read()  # 不常用 2G

# data = f.readline() # readline() 只读取一行
# data1 = f.readline()
# data = f.readlines()  # 将每一行数据单独放在列表中

# print(data)

f = open(file="baidu_x_system.log", mode="r", encoding="utf-8")
data = f.readlines()
dz = dict()
for cs in data:
    t = cs.split(" ", 1)[0]
    if t in dz:
        dz[t] += 1
    else:
        dz[t] = 0
print(dz)
f.close()
















