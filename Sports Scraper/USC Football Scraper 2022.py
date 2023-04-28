# -*- coding: utf-8 -*-
"""
This is a web scraper made to collect some of the statistics for the
USC football team, for the year 2020.
"""

import re
import requests
import numpy as np
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

school = 'south-carolina'
table_data = []
offense = []
defense = []
difference = ['']
#row_headers = ['G','Cmp','Att','Pct','Yds','TD','Att','Yds','Avg','TD','Plays','Yds','Avg','Pass','Rush','Pen','Tot','No.','Yds','Fum','Int','Tot']
head =[]


#def get_data(school):
url = "https://www.sports-reference.com/cfb/schools/"+school+"/2022.html"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
r = requests.get(url, headers=headers)#, proxies=proxies
content = r.content
soup = BeautifulSoup(content, features='lxml')
#print(soup)

t = soup.findAll('table', attrs={'id':'team'})
# print(t)


#row = t.find('td', attrs={'right'})
#print(row)
  
for h in soup.findAll('th', attrs={'class':'poptip right'}):
    text_head= h.get_text
    th= h['data-tip']
    head.append(th)
    
# print(head)

for row in soup.findAll('td', attrs={'right'}):
    text_TableData = row.get_text()
    table_data.append(text_TableData)
    
for i in table_data[0:22]:
    offense.append(i)
    
for j in table_data[22:44]:
    defense.append(j)
    
for k in table_data[45:]:
    difference.append(k)
    
dict = {"Split":head,"Offense":offense, "Defense":defense, "Difference":difference}
df = pd.DataFrame.from_dict(dict, orient="index")


df = df.transpose() #change me to swap columns and rows
df.to_csv('usc_football_stats.csv', index=True)

#to get the attribute: offense['data-stat']
