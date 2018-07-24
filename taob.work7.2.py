# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 13:56:01 2018

@author: Administrator
"""

url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180718&ie=utf8&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
def th(a):
        print(str(a+1)+'货品信息:')
        title=data['mods']['itemlist']['data']['auctions'][a]['title']
        print('标题:'+str(title))
        price=data['mods']['itemlist']['data']['auctions'][a]['view_price']
        print('价格:'+str(price))
        loc=data['mods']['itemlist']['data']['auctions'][a]['item_loc']
        print('产地:'+str(loc))
        sales=data['mods']['itemlist']['data']['auctions'][a]['view_sales']
        print('销量:'+str(sales))
for a in range(0,35):
    th(a)      
    if (a+1)%4==0:
        print('#'*70)
print('包邮的商品有：')          
for a in range(0,35):
    if float(data['mods']['itemlist']['data']['auctions'][a]['view_fee'])==0:
        print('第'+str(a+1)+'件商品包邮')
print('所有商品的价格如下：')
ls=[]
for a in range(0,35):
    x=float(data['mods']['itemlist']['data']['auctions'][a]['view_price'])
    ls.append(x)
print(ls)
print('价格由低到高如下：')
l=sorted(ls)
print(l)
print('价格由高到低如下：')
h=reversed(l)
print(list(h))
sa=[]
def sales():
    for a in range(0,35):
        sl=data['mods']['itemlist']['data']['auctions'][a]['view_sales']
        s=int(sl[0:-3])
        sa.append(s)
    return sa
sales()
print('所有商品销量如下：')
print(sa)
print('销量由高到低如下：')
sale=sorted(sa)
print(sale)