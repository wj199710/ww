# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:14:46 2018

@author: zhangjiaoli
"""

url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)

#价格排序
pr1=[]
for x in range(0,36):
    price=float(data['mods']['itemlist']['data']['auctions'][x]['view_price'])
    pr1.append(price)
    a=sorted(pr1)
print('价格从高到低')
b=list(reversed(a))
print(b)
#商品销量排序
pr1=[]
for y in range(0,36):
    price=float(data['mods']['itemlist']['data']['auctions'][y]['view_sales'])
    pr1.append(price)
    a=sorted(pr1)
print('价格从高到低')
b=list(reversed(a))
print(b)

    
    