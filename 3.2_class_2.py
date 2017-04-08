#coding=utf-8

class Melo(object):
    def __init__(self, age):
        print 'hello1'

    def __new__(cls, age):
        print 'hello2'
        return super(Melo, cls).__new__(cls, age)

t=Melo(20)
