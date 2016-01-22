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
class WorkFactory(object):
    '''
    classdocs
    '''


    def __init__(self):

        self.connectpool=connectpool.getObject()
        self.maintask=sniffertask.snifferTask()
    def dowork(self):
        head,work_result=self.connectpool.getConnect('http://127.0.0.1:80/nmaptool/getwork', 'GET', '')
        jobs=json.loads(work_result)
        if jobs['result']=='1':
            workarray=Job.Converttojobs(jobs['jobs']) 
            self.maintask.add_work(workarray)
            print 'get job'
        else:
            print 'no job'
  
class schedulecontrol:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
 

    def addschedule(self,event, day_of_week='0-7', hour='11',minute='57' ,second='0',id=''):
        if id=='':
            id=str(time.strftime("%Y-%m-%d %X", time.localtime()));
        self.scheduler.add_job(event,'cron', day_of_week=day_of_week, hour=hour,minute=minute ,second=second,id=id)    
    def removeschedule(self,id):
        self.scheduler.remove_job(id)       
if __name__ == "__main__":   
    temp=schedulecontrol()
    tempw=WorkFactory()
    temp.addschedule(tempw.dowork,'0-7','0-23','0-59','*/5')
    while True:
        pass
    







            