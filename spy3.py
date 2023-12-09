# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:31:49 2023

@author: User
"""

##########台銀牌告匯率擷取##########
import requests
from bs4 import BeautifulSoup
import csv
import time
from os.path import exsits

html=requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
