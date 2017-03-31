#coding=utf-8
import lxml.html
import urllib2

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
tree=lxml.html.fromstring(html)
#print lxml.html.tostring(tree,pretty_print=True)
td=tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
print td.text_content()
