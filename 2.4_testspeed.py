#coding=utf-8
#This program can test the speed of RE(C),BS(Python) and lxml(C).
import time
import urllib2
import re
from bs4 import BeautifulSoup
import lxml.html

FIELDS = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', 'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')

def regex_scraper(html):
    results = {}
    for field in FIELDS:
        results[field] = re.search('<tr id="places_{}__row">.*?<td class="w2p_fw">(.*?)</td>'.format(field), html).groups()[0]
    return results

def beautiful_soup_scraper(html):
    soup = BeautifulSoup(html, 'html.parser') 
    results = {}
    for field in FIELDS:
        results[field] = soup.find('table').find('tr', id='places_{}__row'.format(field)).find('td', class_='w2p_fw').text
    return results

def lxml_scraper(html):
    tree = lxml.html.fromstring(html)
    results = {}
    for field in FIELDS:
        results[field] = tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content()
    return results

times = {}
html = urllib2.urlopen('http://example.webscraping.com/view/47').read()
for name, scraper in ('Regular expressions', regex_scraper), ('Beautiful Soup', beautiful_soup_scraper), ('Lxml', lxml_scraper):
    times[name] = []
    start = time.time()
    for i in range(100):
        if scraper == regex_scraper:
            re.purge()#RE will use cache so we purge(clean) it.
        result = scraper(html)# check scraped result is as expected
        assert(result['area'] == '9,596,960 square kilometres')
        times[name].append(time.time() - start)# record end time of scrape and output the total
    end = time.time()
    print '{}: {:.2f} seconds'.format(name, end - start)
