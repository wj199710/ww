# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 17:28:40 2018

@author: Administrator
"""

ls=open('all_school.txt',encoding='utf-8').readlines()
schoolls=[]
for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
    
import urllib.request as r

url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}
f=open('上海招生人数.txt','a',encoding='utf-8')
i=0
for schoolid in schoolls:
    for kemu in [1,2]:
        req=r.Request(url,data='id={}&type={}&city=31&state=1'.format(schoolid,kemu).encode(),headers=headers)
        f.write(r.urlopen(req).read().decode('utf-8','ignore')+'\n')
        i=i+1
        print(str(i)+'条爬取成功')
f.close()
print('爬取完毕')