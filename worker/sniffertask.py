#!/usr/bin/python
#coding:utf-8
from spidertool.ThreadTool import ThreadTool
import datetime
import time
import spidertool.connectpool
from spidertool.TaskTool import TaskTool
import  sniffertool
import spidertool.webtool as webtool
snifferinstance=None
def getObject():
    global snifferinstance
    if snifferinstance is None:
        snifferinstance=snifferTask(1)
    return snifferinstance
class snifferTask(TaskTool):
    def __init__(self,isThread=1):
        TaskTool.__init__(self,isThread)
        self.sniffer= sniffertool.SniffrtTool()
        self.set_deal_num(5)
    def task(self,req,threadname):
        print threadname+'执行任务中'+str(datetime.datetime.now())
        jobid=req.getJobid()
        hosts=req.getJobaddress();
        ports=req.getPort()
        arguments=req.getArgument()
#         isjob=req.getisJob()
#         if isjob=='1':
#             tempresult=jobcontrol.jobupdate(jobstatus='3',taskid=jobid,starttime=webtool.getlocaltime())
        ans = self.sniffer.scanaddress([hosts], [str(ports)], arguments)
#         print threadname+'任务结束'+str(datetime.datetime.now())
#         if isjob=='1':
#             tempresult=jobcontrol.jobupdate(jobstatus='5',taskid=jobid,finishtime=webtool.getlocaltime())
        return ans
    
if __name__ == "__main__":   
    pass
#   print b



