import urllib2
def download(url):
    print 'Downloading:',url
    try:
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Donwnload error:',e.reason
        html=None
    return html
download('http://www.baidu.com')

#this 'download' can used for every 'urllib2' web-scraping program. 
