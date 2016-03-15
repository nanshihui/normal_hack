#!/usr/bin/python
#coding:utf-8
from httpdect import headdect
from poc_file import pocdect
def identify_main(head='',context='',ip='',port='',productname=''):
    keywords=''
    hackinfo=''
    keywords,hackinfo=headdect.dect(head=head,context=context,ip=ip,port=port)
    keywords,hackinfo=pocdect.dect(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo)
    
#    dedeCMS()
#检测网站的产品    

    return keywords,hackinfo
