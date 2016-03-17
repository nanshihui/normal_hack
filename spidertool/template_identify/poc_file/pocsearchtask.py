#!/usr/bin/python
#coding:utf-8
#!/usr/bin/python
#coding:utf-8
from spidertool.ThreadTool import ThreadTool
import datetime
import time
from lib.logger import initLog
from spidertool import Sqldata,portscantool,connectpool,SQLTool,Sqldatatask,config,webconfig
from spidertool.TaskTool import TaskTool
import MySQLdb

from plugins import default 

pocscantaskinstance=None
def getObject():
    global pocscantaskinstance
    if pocscantaskinstance is None:
        pocscantaskinstance=PocsearchTask(1)
    return pocscantaskinstance
class PocsearchTask(TaskTool):
    def __init__(self,isThread=1,deamon=False,islocalwork=config.Config.islocalwork):
        TaskTool.__init__(self,isThread,deamon=deamon)
        logger = initLog('WebDect.log', 2, True)
        self.pocscan=default.PocController(logger=logger)
        self.config=config.Config
        self.set_deal_num(5)
#         self.islocalwork=islocalwork

        self.webconfig=webconfig.WebConfig
    def task(self,req,threadname):
        print threadname+'POC检测任务启动'+str(datetime.datetime.now())
        
        head=req[0]
        context=req[1]
        ip=req[2]
        port=req[3]
        productname=req[4]
        keywords=req[5]
        hackinfo=req[6]
        self.pocscan.detect(head=head, context=context, ip=ip, port=port, productname=productname, keywords=keywords, hackinfo=hackinfo)
        
        print threadname+'POC检测任务结束'+str(datetime.datetime.now())
        
        
        
        ans=''
        
        return ans

if __name__ == "__main__":

    pass




