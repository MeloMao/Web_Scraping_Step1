#coding=utf-8

class Melo:
    def __init__(self,age=20):
        print'hello1'
    def __new__(cls):
        print'hello2'

t=Melo()
