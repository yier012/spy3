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


    