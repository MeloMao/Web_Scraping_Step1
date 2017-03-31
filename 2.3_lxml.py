#coding=utf-8
import lxml.html

html='''<html><head><title>melo</head><body>test</html>'''
tree=lxml.html.fromstring(html)
print lxml.html.tostring(tree,pretty_print=True)
