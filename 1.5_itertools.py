#coding=utf-8
import urllib2
import itertools

def download(url):
    print 'Downloading:',url
    try:
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Donwnload error:',e.reason
        html=None
    return html

for page in itertools.count(1):
    url='http://example.webscraping.com/view/-%d' % page
    html=download(url)
    #print html
    if html is None:
        break
    else:
        pass