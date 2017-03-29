#coding=utf-8
import urllib2
from bs4 import BeautifulSoup

def download(url):
    print 'Downloading:',url
    try:
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Donwnload error:',e.reason
        html=None
    return html

url='http://example.webscraping.com/view/47'
html=download(url)
soup=BeautifulSoup(html,"lxml")
print soup.prettify()#print all of this page
print soup.title
print soup.head
print soup.a
