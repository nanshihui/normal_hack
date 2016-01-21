#!/usr/bin/python
#coding:utf-8
import uuid
from spidertool import webtool
class Job(object):
    @staticmethod
    def Converttojobs(array):
        jobs=[]
        if array is None:
            return jobs
        for ajob in array:
            jobname=ajob.get('jobname','')
            jobaddress=ajob.get('jobaddress','')
            priority=ajob.get('priority','')
            starttime=ajob.get('starttime','')
            username=ajob.get('username','')
            jobport=ajob.get('jobport','')
            jobstatus=ajob.get('jobstatus','')
            jobid=ajob.get('jobid','')
            result=ajob.get('result','')
            endtime=ajob.get('endtime','')
            createtime=ajob.get('createtime','')
            argument=ajob.get('argument','')
            forcesearch=ajob.get('forcesearch','')
            isjob=ajob.get('isjob','')
            job=Job(jobname,jobaddress,priority,starttime,username,jobport,jobstatus,jobid,result,endtime,createtime,argument,forcesearch,isjob)
            jobs.append(job)
        return jobs 
    def __init__(self,jobname='',jobaddress='',priority='1',starttime='',username='',jobport='',jobstatus='1',jobid='',result='',endtime='',createtime='',argument='',forcesearch='',isjob='1'):
        '''
        Constructor
        '''
#         jobstatus=1 //未启动
#         jobstatus=2 //排队中
#         jobstatus=3 //正在进行
#         jobstatus=4 //挂起
#         jobstatus=5 //已完成
#         jobstatus=6 //已终止
        self.jobname=jobname
        self.jobaddress=jobaddress
        self.priority=priority
        self.starttime=starttime
        self.username=username
        self.isjob=isjob
        if forcesearch!='':
            self.forcesearch=forcesearch
            
        else:
            self.forcesearch='0'
        if createtime!='':
            self.createtime=createtime
        else:
            self.createtime=webtool.getlocaltime()
        if jobid!='':
            self.jobid=jobid
        else:
            self.jobid=uuid.uuid1()
        self.jobport=jobport
        self.jobstatus=jobstatus
        self.result=result
        self.endtime=endtime
        self.argument=argument
    def setPriority(self,priority):
        self.priority=priority
    def setArgument(self,argument):
        self.argument=argument
        
    def setResult(self,result):
        self.result=result
    def setJobstatus(self,jobstatus):
        self.jobstatus=jobstatus
    def getForcesearch(self):
        return self.forcesearch
    def getUsername(self):
        return self.username
    def getJobname(self):
        return self.jobname
    def getJobaddress(self):
        return self.jobaddress
    def getJobid(self):
        return self.jobid
    def getResult(self):
        return self.result
    def getPort(self):
        return self.jobport
    def getPriority(self):
        return self.priority 
    def getisJob(self):
        return self.isjob 
    def getStatus(self):
        return self.jobstatus
    def getStarttime(self):
        return self.starttime
    def getCreatetime(self):
        return self.createtime
    def getArgument(self):
        return self.argument
    