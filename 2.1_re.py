#coding=utf-8

import re
import urllib2

def download(url):
    print 'Downloading:',url
    try:
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Donwnload error:',e.reason
        html=None
    return html

url='http://example.webscraping.com/view/China-47'
html=download(url)
print re.findall('<td class="w2p_fw">(.*?)</td>',html)[4]
