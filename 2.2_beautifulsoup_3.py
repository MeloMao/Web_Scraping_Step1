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
#print soup.prettify()
tr=soup.find(attrs={'id':'places_area__row'})
td=tr.find(attrs={'class':'w2p_fw'})
area=td.text
print area
