# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:43:22 2019

@author: Administrator
"""
import requests
import json
url='https://ssc.sjtu.edu.cn/api/chart/408e24cc/apply/filter'
#headers={'User-Agent':'Mozilla/5.0'}
begin_num=''  #your student number
jieguo=[]
for i in range(10):
    info=[]
    point=0
    number=str(begin_num+i)
    payload={"filter":{"pageSize":50,"pageNum":1,"type":13,"sorts":[],"queries":[],"queryKey":""},"accurateQuery":[{"queId":10902,"queType":2,"searchKey":number}]}
    t=requests.post(url,data=json.dumps(payload))
    res=t.json()
    Id=number
  
    total_results=res.get('resultAmount',0)
    if total_results >0:
        info.append(Id)
        name=res.get('result','')[0].get('answers','')[0].get('values')[0].get('value')
        info.append(name)
        
        for j in range(total_results):
            point+=float(res.get('result','')[j].get('answers','')[5].get('values')[0].get('value'))
            
        info.append(point)
    else:
        print('none data',end='\t')
    if info:
        jieguo.append(info)

