#!/usr/bin/env python
# encoding: utf-8
from spidertool import Sqldatatask,Sqldata,SQLTool,webconfig
import spidertool.config as config
from model import uploaditem
import time
from worker import uploadtask
islocalwork=config.Config.islocalwork
def storedata(ip='',port='',hackinfo=None,islocalwork=config.Config.islocalwork):
    
    localtime=str(time.strftime("%Y-%m-%d %X", time.localtime()))
    insertdata=[]
    hackinfo=SQLTool.escapewordby(str(hackinfo))
    extra=' on duplicate key update  hackinfo=\''+hackinfo+'\' , timesearch=\''+localtime+'\''
             
    insertdata.append((str(ip),port,hackinfo,str(port)))
 
 
    
    dic={"table":config.Config.porttable,"select_params":['ip','port','hackinfo','portnumber'],"insert_values":insertdata,"extra":extra}
                
    if islocalwork==0:
        work=[]
        tempdata={"func":'inserttableinfo_byparams',"dic":dic}
        jsondata=uploaditem.UploadData(url=webconfig.WebConfig.upload_ip_info,way='POST',params=tempdata)
        work.append(jsondata)
        temp=uploadtask.getObject()
        temp.add_work(work)
                     
    else:
        sqlTool=Sqldatatask.getObject()
        sqldatawprk=[]
        tempwprk=Sqldata.SqlData('inserttableinfo_byparams',dic)
        sqldatawprk.append(tempwprk)
        sqlTool.add_work(sqldatawprk)   
    
def storeresult(result=None):
    print '----------------------------------------'
    print '发现漏洞'
    print '位置:'+result['VerifyInfo']['URL']
    print '类型:'+result['VerifyInfo']['type']
    print 'payload:'+result['VerifyInfo']['payload']
    
    return True
