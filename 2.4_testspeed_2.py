#coding=utf-8
#This program can test te speed of RE(C),BS(Python) and lxml(C).
import time
import re
from bs4 import BeautifulSoup
import lxml.html

FIELDS = ('help')

def regex_scraper(html):
    results = {}
    for field in FIELDS:
        results[field] = re.search('help', html)
    return results

def beautiful_soup_scraper(html):
    soup = BeautifulSoup(html, 'html.parser') 
    results = {}
    for field in FIELDS:
        results[field] = soup.find('help')
    return results

def lxml_scraper(html):
    tree = lxml.html.fromstring(html)
    results = {}
    for field in FIELDS:
        results[field] = tree.cssselect('help')
    return results

times = {}
html = '''<body>help</body>'''
for name, scraper in ('Regular expressions', regex_scraper), ('Beautiful Soup', beautiful_soup_scraper), ('Lxml', lxml_scraper):
    times[name] = []
    start = time.time()
    for i in range(1000):
        if scraper == regex_scraper:
            re.purge()#RE will use cache so we purge(clean) it.
        result = scraper(html)# check scraped result is as expected
        times[name].append(time.time() - start)# record end time of scrape and output the total
    end = time.time()
    print '{}: {:.2f} seconds'.format(name, end - start)
