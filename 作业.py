import  xlrd
import  pymysql
import  xlwt
from DBUtils import*
def pm():
    wd = xlrd.open_workbook("12月份衣服销售数据.xlsx", encoding_override=True)
    # 2.打开您要操作的选项卡
    st = wd.sheet_by_name("12月份各种服饰销售情况")
    rows = st.nrows  # 获取行数
    cols = st.ncols  # 获取列数
    for i in range(1,rows):
        data = st.row_values(i)
        sql = "insert into tea values(%s,%s,%s,%s,%s)"
        update(sql,data)
pm()
def pt():
    tea = ["日期","服装名称","价格/件","库存数量","销售量/日"]
    #获取数据库中所有数据
    sql = "select * from tea"
    param = []
    data = select(sql,param,mode="all",size=1)
    print(data)
    rows = len(data)
    cols = len(data[0])
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet1 = workbook.add_sheet("12衣服销售情况")
    for i in range(rows+1):
        for j in range(cols):

            if i == 0:
                sheet1.write(i, j, tea[j])
            else:
                sheet1.write(i,j,data[i-1][j])
    workbook.save("D:\workspace\pythonProject\day9\dame.xls")
    print("创建excel成功：")

pt()