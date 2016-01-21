#!/usr/bin/python
#coding:utf-8
'''
Created on 2016年1月21日

@author: sherwel
'''
import sys
sys.path.append("..")
import spidertool.connectpool as connectpool
import json
import time
from model.job import Job
class WorkFactory(object):
    '''
    classdocs
    '''


    def __init__(self):

        self.connectpool=connectpool.getObject()

    def dowork(self):
        head,work_result=self.connectpool.getConnect('http://127.0.0.1:82/nmaptool/getwork', 'GET', '')
        jobs=json.loads(work_result)
        if jobs['result']=='1':
            workarray=Job.Converttojobs(jobs['jobs']) 
            print 'get job'
        else:
            time.sleep(10)
            self.dowork()
  
        
if __name__ == "__main__":   

    temp=WorkFactory()
    temp.dowork()




            