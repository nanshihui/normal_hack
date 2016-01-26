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
from spidertool.TaskTool import TaskTool
import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import os 
from model.job import Job
import sniffertask
uploadworker=None
def getObject():
    global uploadworker
    
    if uploadworker is  None:
        uploadworker=UploadTask()
        uploadworker.set_deal_num(1)
    return uploadworker
         
class UploadTask(TaskTool):
    '''
    classdocs
    '''


    def __init__(self,isThread=1):
        TaskTool.__init__(self,isThread)
        self.connectpool=connectpool.getObject()
    def task(self,req,threadname):
        way=req.getway()
        params=req.getparams()
        url=req.geturl()
        head,work_result=self.connectpool.getConnect(url,way, params)

        return work_result

