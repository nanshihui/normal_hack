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
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import os 
from model.job import Job
import sniffertask
class UploadWorker(object):
    '''
    classdocs
    '''


    def __init__(self):

        self.connectpool=connectpool.getObject()
        self.maintask=sniffertask.snifferTask()
    def dowork(self,params,way):

        head,work_result=self.connectpool.getConnect('http://127.0.0.1:80/nmaptool/uploadwork', 'GET', '')
        jobs=json.loads(work_result)
        if jobs['result']=='1':
            return True
        else:
            return False
        
        	