# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 19:17:29 2022

@author: Micha
"""
import pandas as pd
import numpy as np
import re
import time
from bs4 import BeautifulSoup
import requests
import statistics

import configparser

from SQLConnectorTemplate import create_connection
from SQLConnectorTemplate import execute_query



config = configparser.ConfigParser()
config.read('config.ini')
ip_addr = config['mysql']['ip_addr']
username = config['mysql']['username']
password = config['mysql']['password']
port = config['mysql']['port']
database = config['mysql']['database']


items = []
Dict = dict({})
pageNumber = 9
tempDF = pd.DataFrame()
connection = create_connection(ip_addr,username,password,port,database)

def sortBySPrice():
    temp = df.sort_values(by='salePrice',ascending=False)
    print(temp)
def sortByNPrice():
    temp = df.sort_values(by='normalPrice',ascending=False)
    print(temp)
def sortByDaysLeft():
    temp = df.sort_values(by="endDateOfSale", ascending=False)
    print(temp)
def sortByScore(dataF):
    temp = dataF.sort_values(by="metaScore", ascending=False)
    print(temp)    
def findWhere(column, value):
    temp = df[column].isin([value])
    tempDF = pd.DataFrame(temp)
    print(df[temp])
def insertToSQL(anId,aName,sPrice,nPrice,Mscore):
    insert ="INSERT INTO `scrapingDB1`.`PS4ScrappedData` (`id`, `Game Name`, `Sale Price`, `Normal Price`, `MetaScore`) VALUES ('"+str(anId)+"', '"+aName+"', '"+str(sPrice)+"', '"+str(nPrice)+"', '"+str(Mscore)+"');"
    execute_query(connection, insert)
    connection.commit()
def get_data(PageNum):
    url = 'https://psdeals.net/us-store/discounts/'+str(PageNum)+'?platforms=ps4&sort=rating-desc'
    headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    r = requests.get(url, headers=headers)    
    content = r.content
    soup2 = BeautifulSoup(content, features ="lxml")
    count =0
    print(soup2)
    for tag in soup2.findAll('a', attrs={'class':'game-collection-item-link'}):
        # print(tag)
        name = tag.find('span', attrs={'itemprop':'name'}).text
        salePrice= tag.find('span', attrs={'itemprop':'price'}).text
        normalPrice = tag.find('span', attrs={'class':'game-collection-item-price strikethrough'}).text
        normalPrice = normalPrice[normalPrice.index("$")+1:]
        
        salePrice = float(salePrice)
        normalPrice = float(normalPrice)
        endDateOfSale = tag.find('span', attrs={'class':'game-collection-item-end-date'})
        if(endDateOfSale):
            endDateOfSale = endDateOfSale.text
            print(endDateOfSale)
            if "day" in endDateOfSale:
                #daysLeft = endDateOfSale[endDateOfSale.index("in ")+3:endDateOfSale.index("day")]
                daysLeft = endDateOfSale[endDateOfSale.index("in ")+3:]
            elif "hour" in endDateOfSale:
                daysLeft = endDateOfSale[endDateOfSale.index("in ")+3:]
            if(daysLeft == " a"):
                daysLeft = 1
        else:
            daysLeft ="None"
            
        metaScore = tag.find('div', attrs={'class':'game-collection-item-metascore'})
        if(metaScore):
            mScore = int(metaScore.text)
        else:
            mScore = int("000")
            

        item = {"Name":name,"salePrice":salePrice,"normalPrice":normalPrice, "endDateOfSale":daysLeft, "metaScore":mScore}
        items.append(item.copy())
        print(item)
        insertToSQL(count, name, salePrice, normalPrice, mScore)
        count+=1
for i in range(1,pageNumber):
    get_data(i)
df = pd.DataFrame(items)
print(df)
