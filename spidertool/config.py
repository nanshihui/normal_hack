#!/usr/bin/python
#coding:utf-8
class Config(object):
	#config file #
	host='localhost'
	username='root'
	passwd=''
	database='datap'
	port=3306
	charset='utf8'
	cachemax=30
	cachemin=1
	iptable='ip_maindata'
	porttable='snifferdata'
	usertable='user_table'
	tasktable='taskdata'
	iptable='ip_maindata'
	islocalwork=0#分布任务是否直接存储，０必须要提交WEB存储数据，１直接存储数据
		