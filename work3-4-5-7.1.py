# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:10:31 2018

@author: Administrator
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=dali,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json
data=json.loads(data)
def weather(day,a):
    print(str(day)+'号18点的天气信息:')
    print('温度：'+str(data['list'][a]['main']['temp']))
    print('天气情况：'+str(data['list'][a]['weather'][0]['description']))
    print('气压：'+str(data['list'][a]['main']['pressure']))
    print('最高温：'+str(data['list'][a]['main']['temp_max']))
    print('最低温：'+str(data['list'][a]['main']['temp_min']))
    t=float(data['list'][a]['main']['temp'])
    a=data['list'][a]['weather'][0]['description']
    if t>=30.00 :
        print('温馨提示：注意防晒')
    elif t>=15.00 and t<30.00:
        print('温馨提示：适宜外出')
    elif t<15.00:
        print('温馨提示：注意保暖')
    else:
        print('输出错误')
    
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)
weather(5,34)

city=input('Please enter the name of the city you want to inquire.')
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url.format(city)).read().decode('utf-8','ignore')
import json
data=json.loads(data)
mian=data['list'][0]['weather'][0]['main']
print('The weather is the case：'+main)

print('温度折线图如下：')
def tu(day,a):
    return(str(day)+':'+'-'*int(data['list'][a]['main']['temp']))
print(tu(1,2))
print(tu(2,10))
print(tu(3,18))
print(tu(4,26))
print(tu(5,34))
print('所有温度如下：')
print(data['list'][2]['main']['temp'],data['list'][10]['main']['temp'],data['list'][18]['main']['temp'],data['list'][26]['main']['temp'],data['list'][34]['main']['temp'])
print('对温度排序如下：')
temp=[data['list'][2]['main']['temp'],data['list'][10]['main']['temp'],data['list'][18]['main']['temp'],data['list'][26]['main']['temp'],data['list'][34]['main']['temp']]
print(sorted([data['list'][2]['main']['temp'],data['list'][10]['main']['temp'],data['list'][18]['main']['temp'],data['list'][26]['main']['temp'],data['list'][34]['main']['temp']]))