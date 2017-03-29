#coding=utf-8
from bs4 import BeautifulSoup

html='''<html><head><title>melo</head><body>test</html>'''
soup=BeautifulSoup(html,"html.parser")
print soup.prettify()
