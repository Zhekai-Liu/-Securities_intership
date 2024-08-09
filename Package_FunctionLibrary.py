import pandas as pd
from EmQuantAPI import *
import numpy as np

def EtoDic(file_path,fir,sec):
    zdf = pd.read_excel(file_path, dtype={fir: str,sec: str})
    ZDict = dict(zip(zdf[fir], zdf[sec]))
    return ZDict

def sort(d):
    f = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return f

def translate_the_dic(df):
    d = df.Data
    for k in d:
        d[k] = d[k][0]
    #f = sorted(d.items(), key=lambda x: x[1], reverse=True)
    f = sort(d)
    return f



def cauculate(ds,de):
    dfs = translate_the_dic(ds)
    dfe = translate_the_dic(de)
    df = {}
    dfss = dict(dfs)
    dfee = dict(dfe)

    for k in dfs:
        df[k[0]] = ((dfee[k[0]] / dfss[k[0]]) - 1)*100

    return df


def excel(f, dic):
    df = dict(f)
    insert = []
    for i in df:
        insert.append(dic[i])

    fp = pd.DataFrame([df]).T
    fp.insert(0, '行业名称', insert)
    fp.reset_index(inplace=True)
    fp.rename(columns={'index': '股票代码', 0: '涨跌幅'}, inplace=True)
    fp.to_excel('行业行情.xlsx')
    ff = pd.read_excel('行业行情.xlsx', index_col=1)

    ff.drop(['Unnamed: 0'], inplace=True, axis=1)

    return ff

def standard(x, e, std):
    score = (x - e)/std
    return score

def to_stan(frame, col_name):
    aver = np.mean(frame[col_name])
    sd = frame[col_name].std()

    return aver, sd


def roll(r):
    data = c.csd(r, "CLOSE,PCTCHANGE", "2020-08-09", "2023-08-09", "period=1,adjustflag=1,curtype=1,order=1,market=CNSESH,Ispandas=1")
    print(data)
    data['买入120天涨跌幅'] = data['CLOSE']/data['CLOSE'].shift(120) - 1
    sum_day = (data['买入120天涨跌幅'] > 0).sum()
    count = data['买入120天涨跌幅'].count()
    aver = np.mean(data['买入120天涨跌幅'])

    data['日波动率'] = data['PCTCHANGE'].rolling(120).std()
    vola = np.mean(data['日波动率'])*(120**0.5)
    print(data)
    return sum_day, count, aver, 1/vola

