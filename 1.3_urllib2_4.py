import urllib2
response = urllib2.urlopen('http://example.webscraping.com/robots.txt')
html = response.read()
print html
