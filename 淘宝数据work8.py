# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:09:13 2018

@author: Administrator
"""
import urllib.request as r
f=open('xiamenqunzi.txt','w',encoding='utf-8')
for p in range(0,101):
    url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&style=grid&loc=%E5%8E%A6%E9%97%A8'+'&s=((2p-2)*22)'+'&ajax=true'
    data=r.urlopen(url).read().decode('utf-8')
    print('第'+str(p+1)+'页商品信息爬取成功')
    f.write(data+'\n')
f.close()