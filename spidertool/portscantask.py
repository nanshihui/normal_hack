#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import connectpool
import portscantool
import SQLTool
import Sqldata
from TaskTool import TaskTool
import MySQLdb
import Sqldatatask
import config,webconfig
from model import uploaditem

portscantskinstance=None
def getObject():
    global portscantskinstance
    if portscantskinstance is None:
        portscantskinstance=PortscanTask(1)
    return portscantskinstance
class PortscanTask(TaskTool):
    def __init__(self,isThread=1,deamon=False,islocalwork=config.Config.islocalwork):
        TaskTool.__init__(self,isThread,deamon=deamon)
        
        self.sqlTool=Sqldatatask.getObject()
        self.connectpool=connectpool.getObject()
        self.portscan=portscantool.Portscantool()
        self.config=config.Config
        self.set_deal_num(5)
        self.islocalwork=islocalwork
        from worker import uploadtask
        self.uploadwork=uploadtask.getObject()
        self.webconfig=webconfig.WebConfig
    def task(self,req,threadname):
        print threadname+'执行任务中'+str(datetime.datetime.now())

#         print req[0],req[1],req[2],req[3]
        if req[3]!='open':
            return ''
        ip=req[1]
        port=req[2]
        productname=req[4]
        head=None
        ans=None
        hackinfo=''
        keywords=''
        if req[0]=='http' or req[0]=='https':
            if ip[0:4]=='http':
                address=ip+':'+port
            else:
                if  port=='443':
                    address='https'+'://'+ip+':'+port
                else:
                    
                    address=req[0]+'://'+ip+':'+port
            print address
            head,ans = self.connectpool.getConnect(address)
            from template_identify import page_identify
            keywords,hackinfo=page_identify.identify_main(head=head,context=ans,ip=ip,port=port,productname=productname,protocol=req[0])
        else:
            head,ans,keywords,hackinfo=self.portscan.do_scan(ip,port,req[0],productname=productname)
        

        localtime=str(time.strftime("%Y-%m-%d %X", time.localtime()))
        insertdata=[]
        temp=str(ans)
        head=SQLTool.escapeword(head)
        msg=SQLTool.escapeword(temp)
        hackinfomsg=SQLTool.escapeword(hackinfo)
        keywords=SQLTool.escapewordby(keywords)
        insertdata.append((ip,port,localtime,str(head),msg,str(port),hackinfomsg,keywords))
                                         
        extra=' on duplicate key update  detail=\''+msg+'\' ,head=\''+str(head)+'\', timesearch=\''+localtime+'\',hackinfo=\''+hackinfomsg+'\',keywords=\''+str(keywords)+'\''
        sqldatawprk=[]
        dic={"table":self.config.porttable,"select_params":['ip','port','timesearch','detail','head','portnumber','hackinfo','keywords'],"insert_values":insertdata,"extra":extra}
        
        if self.islocalwork==0:
            tempdata={"func":'inserttableinfo_byparams',"dic":dic}
            jsondata=uploaditem.UploadData(url=self.webconfig.upload_port_info,way='POST',params=tempdata)
            sqldatawprk.append(jsondata)
            self.uploadwork.add_work(sqldatawprk)
        else:
        
        
            tempwprk=Sqldata.SqlData('inserttableinfo_byparams',dic)
            sqldatawprk.append(tempwprk)
            self.sqlTool.add_work(sqldatawprk)
#         inserttableinfo_byparams(table=self.config.porttable,select_params=['ip','port','timesearch','detail'],insert_values=insertdata,extra=extra)


#         self.sqlTool.closedb()
        print threadname+'任务结束'+str(datetime.datetime.now())
        
        
        
        
        
        return ans

if __name__ == "__main__":

    pass




