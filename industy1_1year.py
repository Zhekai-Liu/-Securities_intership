from EmQuantAPI import *
import industry_funtion as ex



codes = "801010.SWI,801030.SWI,801040.SWI,801050.SWI,801080.SWI,801110.SWI,801120.SWI,801130.SWI,801140.SWI,801150.SWI,801160.SWI,801170.SWI,801180.SWI,801200.SWI,801210.SWI,801230.SWI,801710.SWI,801720.SWI,801730.SWI,801740.SWI,801750.SWI,801760.SWI,801770.SWI,801780.SWI,801790.SWI,801880.SWI,801890.SWI,801950.SWI,801960.SWI,801970.SWI,801980.SWI"
dic = ex.EtoDic('industry.xlsx', '申万一级代码', '申万一级名称')
c.start()

df = c.css(codes, "DIFFERRANGEY", "TradeDate=2023-08-08")

f = ex.translate_the_dic(df)

for k in f:
    print("行业编号：%s   行业名称：%s\t\t近一年涨跌幅：%.2f %%" % (k[0], dic[k[0]], k[1]))

ff = ex.excel(f, dic)
ff.to_excel('一级行业近一年行情.xlsx')

print("运行成功")