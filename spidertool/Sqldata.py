#!/usr/bin/python
#coding:utf-8
class SqlData(object):
    def __init__(self,func,dic,url='',way='GET',params=None):
        '''
        Constructor
        '''
        self.func=func
        self.dic=dic

        self.url=url
        self.way=way
        self.params=params

    def getFunc(self):
        return self.func
    def getDic(self):
        return self.dic
    def getURL(self):
        return self.url
    def getWay(self):
        return self.way
    def getParams(self):
        return self.params
