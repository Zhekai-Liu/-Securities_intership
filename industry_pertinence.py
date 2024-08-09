from EmQuantAPI import *
import pandas as pd
import industry_funtion as ex


dic = ex.EtoDic('industry.xlsx', '申万一级代码', '申万一级名称')
c.start()
codes = [['801170.SWI'], ['801890.SWI'], ['801040.SWI']]
#df = c.csd(codes, "PCTCHANGE", "2018-01-02", "2023-08-09", "period=1,adjustflag=1,curtype=1,order=1,market=CNSESH, Ispandas=1")

def fun(r):
    a = c.csd(r, "PCTCHANGE", "2018-01-02", "2023-08-09", "period=1,adjustflag=1,curtype=1,order=1,market=CNSESH, Ispandas=1")
    a.rename(columns={'PCTCHANGE': dic[r[0]]}, inplace=True)  # 复权单位净值增长率
    a.reset_index(inplace=True)
    a.drop(['CODES'], inplace=True, axis=1)
    a.drop(['DATES'], inplace=True, axis=1)
    return a

dfC = pd.DataFrame()
for k in codes:
    df = fun(k)
    dfC = pd.concat([dfC, df], axis=1)



#ff = pd.read_excel('BHP.xls')
#dfC = pd.concat([dfC, ff], axis=1)
print(dfC)
print(dfC.astype(float).corr())
