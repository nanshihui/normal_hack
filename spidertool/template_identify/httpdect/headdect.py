#!/usr/bin/python
#coding:utf-8
import webdection 
def dect(head='',context='',ip='',port=''):
    webdection
    keywords=''
    hackinfo=''
    w = webdection.WMap(mode=192, logger=None)
    keywords= str(w.detect(ip+':'+str(port)))
    print keywords
    return keywords,hackinfo
