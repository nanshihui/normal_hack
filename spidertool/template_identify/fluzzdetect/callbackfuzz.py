#!/usr/bin/env python
# encoding: utf-8

from spidertool import Sqldatatask,Sqldata,SQLTool,webconfig
import spidertool.config as config
from model import uploaditem
import time
from worker import uploadtask
islocalwork=config.Config.islocalwork
def storedata(ip='',port='',hackinfo=None):

    sqlTool=Sqldatatask.getObject()
    localtime=str(time.strftime("%Y-%m-%d %X", time.localtime()))
    insertdata=[]
     
    hackinfo=SQLTool.escapewordby(str(hackinfo))
    extra=' on duplicate key update  disclosure=\''+hackinfo+'\' , timesearch=\''+localtime+'\''
              
    insertdata.append((str(ip),port,hackinfo,str(port)))
    dic={"table":config.Config.porttable,"select_params":['ip','port','disclosure','portnumber'],"insert_values":insertdata,"extra":extra}

    if islocalwork==0:
        work=[]
        tempdata={"func":'inserttableinfo_byparams',"dic":dic}
        jsondata=uploaditem.UploadData(url=webconfig.WebConfig.upload_ip_info,way='POST',params=tempdata)
        work.append(jsondata)
        temp=uploadtask.getObject()
        temp.add_work(work)

                      
    else:

  
  
        sqldatawprk=[]
                 
        tempwprk=Sqldata.SqlData('inserttableinfo_byparams',dic)
        sqldatawprk.append(tempwprk)
        sqlTool.add_work(sqldatawprk)   
        print 'fuzz 数据存储'
        pass
 
     
     