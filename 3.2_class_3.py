#coding=utf-8

class Test(object):
    def __init__(self):
        print 100

    def __new__(cls):
        print 200
        return super(Test, cls).__new__(cls)

    def __call__(self, x):
        print 300

t = Test()
t(100)
