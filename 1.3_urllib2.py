#coding=utf-8
import urllib2
def download(url):
    return urllib2.urlopen(url).read()
url='http://www.baidu.com'
download('http://www.baidu.com')
print('Done')
