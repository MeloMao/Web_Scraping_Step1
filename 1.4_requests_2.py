#coding=utf-8
import requests
payload={'user':'hrz','passwd':'123'}
r=requests.get('http://jxpt.cuit.edu.cn',params=payload)
print(r.url)

#maybe this program can use for brute force.
