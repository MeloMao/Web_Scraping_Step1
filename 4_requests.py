#coding=utf-8
import requests
r=requests.get('http://github.com/timeline.json')
s=requests.post('http://github.com/post')
t=requests.head('http://github.com/get')
u=requests.put('http://github.com/put')
v=requests.delete('http://github.com/delete')
w=requests.options('http://github.com/get')
print r.text
print ('\n\n\n-----line--------------------------------\n\n\n')
print s.text
print ('\n\n\n-----line--------------------------------\n\n\n')
print t.text
print ('\n\n\n-----line--------------------------------\n\n\n')
print u.text
print ('\n\n\n-----line--------------------------------\n\n\n')
print v.text
print ('\n\n\n-----line--------------------------------\n\n\n')
print w.text
