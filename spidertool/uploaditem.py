#!/usr/bin/python
#coding:utf-8
#用于上传数据的时候，定义的模型
class UploadData(object):
    def __init__(self,url,way,params):
        '''
        Constructor
        '''
        self.url=url
        self.way=way
        self.params=params



    def getURL(self):
        return self.url
    def getWay(self):
        return self.way
    def getParams(self):
        return self.params
