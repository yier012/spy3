# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:31:49 2023

@author: User
"""

##########台銀牌告匯率擷取##########
import requests
from bs4 import BeautifulSoup
import csv
from os.path import exists

html=requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
bsObj=BeautifulSoup(html.content,"lxml")
file_name="E2-1-1-1"+"各國貨幣"+".csv"

for single_tr in bsObj.find("table",{"title":"牌告匯率"}).find("tbody").findAll("tr"):
    cell=single_tr.findAll("td")
    currency_name=cell[0].find("div",{"class":"visible-phone"}).contents[0]
    currency_name=currency_name.replace("\r","")
    currency_name=currency_name.replace("\n","")
    currency_name=currency_name.replace(" ","")
    rate1=cell[1].contents[0]
    rate2=cell[2].contents[0]
    rate3=cell[3].contents[0]
    rate4=cell[4].contents[0]
    
    print(currency_name,rate1)
    if not exists(file_name):
        data=[["貨幣名稱","現金買入","現金買出","即期買入","即期買出"],
              [currency_name,rate1,rate2,rate3,rate4]]
    else:
        data=[[currency_name,rate1,rate2,rate3,rate4]]
    f=open(file_name,"a",newline="")
    w=csv.writer(f)
    w.writerows(data)
f.close()

##########證交所擷取##########
import pandas as pd
df=pd.read_html("https://isin.twse.com.tw/isin/C_public.jsp?strMode=2",
                encoding="big5hkscs",header=0)
newdf=df[0][df[0]["產業別"]>"0"]
newdf=newdf.drop(["CFICode","備註"],axis=1)
df2=newdf["有價證券代號及名稱"].str.split('　',expand=True)
df2=df2.rename(columns={0:"股票代號",1:"股票名稱"})
newdf=newdf.drop(["有價證券代號及名稱"],axis=1)
newdf=df2.join(newdf)
newdf.to_excel('E2-1-1-2-output.xlsx',sheet_name='sheet1',index=False)

##########urllib練習##########
import urllib.request

response=urllib.request.urlopen('http://python.org/')
html=response.read()
print(html)

##########財政部統一發票號碼擷取##########
import urllib
from bs4 import BeautifulSoup
import urllib.request

request_url='https://invoice.etax.nat.gov.tw/'
htmlContent=urllib.request.urlopen(request_url).read()
#print(htmlContent)
soup=BeautifulSoup(htmlContent,"html.parser")
results=soup.find_all("span",class_="font-weight-bold etw-color-red")
subTitle=["特別獎","特獎","頭獎","增開六獎"]
for index,item in enumerate(results[:4]):
    print(">>{0}:{1}".format(subTitle[index],item.text))











    