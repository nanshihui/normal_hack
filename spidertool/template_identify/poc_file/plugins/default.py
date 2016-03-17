#!/usr/bin/env python
# encoding: utf-8


from os.path import dirname, abspath, join, isdir
from os import listdir
from urlparse import urljoin
from re import compile
import callbackresult



class PocController(object):
    def __init__(self, logger=None):
        self.modules_list = [

                {'module_name': 'component'},
 ]


        self.keywords    = {}
        self.rules    = {}
        self.components     = {}
        self.logger      = logger
        self.result=None
        self.loader()
    def __list_plugins(self, module_path):
        return set(map(lambda item: item.endswith(('.py', '.pyc')) and item.replace('.pyc', '').replace('.py', ''), listdir(module_path)))

    def __get_component_plugins_list(self,componentname, module_name):
        path = join(abspath(dirname(__file__)), componentname+'/%s' % module_name)
        plugins_list = self.__list_plugins(path)
        if False in plugins_list:
            plugins_list.remove(False)
        plugins_list.remove('__init__')
        if 't' in plugins_list:
        
            plugins_list.remove('t')
        return plugins_list
    def __get_component_detail_list(self,componentname):
        path = join(abspath(dirname(__file__)), componentname)
        modules_list = set(map(lambda item: isdir(join(path, item)) and item, listdir(path)))
        if False in modules_list:
            modules_list.remove(False)


        return modules_list
    def __load(self, module_name, plugin_name):

        plugin_name = '%s.%s' % (module_name, plugin_name)

        plugin = __import__(plugin_name,globals=globals(), fromlist=['P'])

        self.logger and self.logger.info('Load Plugin: %s.P', plugin_name)
        return plugin.P
    def __load_keywords(self,componentname, module_name):
        module_name = componentname+'.%s' % (module_name)

        module = __import__(module_name,globals=globals(), fromlist=['KEYWORDS'])
        return module.KEYWORDS,componentname
    def __load_rules(self,componentname, module_name):
        module_name = componentname+'.%s' % (module_name)
        module = __import__(module_name,globals=globals(), fromlist=['rules'])
        return module.rules,componentname    
    def __load_component_detail_info(self,module_name='',componentname='',func=None,params=None,text=''):
        try:

            params[module_name] = func(componentname,module_name)
            self.logger and self.logger.info('Module '+text+': %s -> %s', module_name, self.keywords[module_name])
        except Exception,e:
            print e
            params[module_name] = [],componentname
            self.logger and self.logger.info('Module '+text+': %s -> None', module_name)
            pass
    def __load_component_detail_plugins(self, componentname=''):

        modules_list = self.__get_component_detail_list(componentname)
        for module_name in modules_list:
            self.components[componentname][module_name] = []

            for plugin_name in self.__get_component_plugins_list(componentname,module_name):
                
                P = self.__load(componentname+'.%s' % module_name, plugin_name)
                self.components[componentname][module_name].append(P)
                self.__load_component_detail_info(module_name=module_name,componentname=componentname,func=self.__load_keywords,params=self.keywords,text='keywords')
                self.__load_component_detail_info(module_name=module_name,componentname=componentname,func=self.__load_rules,params=self.rules,text='rules')
    def __load_component_plugins(self, modules_list):
        for module_name in modules_list:
            self.components[module_name] = {}
            self.__load_component_detail_plugins(module_name)

    def loader(self):
        self.components = {}
        self.__load_component_plugins(map(lambda module_info: module_info['module_name'], self.modules_list))
    def env_init(self, head='',context='',ip='',port='',productname='',keywords='',hackinfo=''):
        self.init(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo)
    def init(self,  head='',context='',ip='',port='',productname='',keywords='',hackinfo='', **kw):
        POCS = []
        modules_list = []
        
        
        modules_list, _ = self.__match_modules_by_info(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords)
        for modules,conponent in modules_list:
            for item in self.components[conponent][modules]:
                P=item()
                
                if self.__match_rules(pocclass=P,head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo, **kw):
                    POCS.append(P)
                
                
                
                
                self.logger and self.logger.info('Init Plugin: %s', item)
        self.match_POC(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo,POCS=POCS, **kw)
    def match_POC(self,head='',context='',ip='',port='',productname='',keywords='',hackinfo='',POCS=None, **kw):
        haveresult=False
        for poc in POCS:

            result = poc.verify(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo)


            if result['result']:
                haveresult=callbackresult.storedata(ip=ip,port=port,hackinfo=result)
                print '发现漏洞'
                break;


        if haveresult == False:
            print '-----------------------'
            print '暂未发现相关漏洞'
    def __match_rules(self,pocclass=None,head='',context='',ip='',port='',productname='',keywords='',hackinfo='', **kw):

        return pocclass.match_rule(head='',context='',ip='',port='',productname='',keywords='',hackinfo='', **kw)
        
    
    
    
    
    
    
    def __match_modules_by_info(self,head='',context='',ip='',port='',productname='',keywords=''):
        matched_modules = set()
        othermodule=[]
#         for module_name in self.components.keys():
#             othermodule.extend(self.components[module_name].keys())

        kw=keywords#关键词

        for module_name, module_info in self.keywords.items():
            modulekeywords=module_info[0]
            comonentname=module_info[1]
            if not modulekeywords:
                
                
                matched_modules.add((module_name,comonentname))
                continue
            for keyword in modulekeywords:
                if keyword in kw or keyword in productname.lower()  or keyword in head.lower()   :
                    
                    
#                     self.logger and self.logger.info('Match Keyword: %s -> %s', resp.url, keyword)
                    matched_modules.add((module_name,comonentname))
                    break
        for module_name, module_info in self.rules.items():
            rules=module_info[0]
            comonentname=module_info[1]

            if not rules:
                
                print module_name,comonentname
                matched_modules.add((module_name,comonentname))
                continue
            if rules(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo='')  :
                    
                    
#                     self.logger and self.logger.info('Match Keyword: %s -> %s', resp.url, keyword)
                    matched_modules.add((module_name,comonentname))
                    break
# 
#         for match in matched_modules:
#             othermodule.remove(match)
#         print othermodule
        return matched_modules, othermodule



    def detect(self, head='',context='',ip='',port='',productname='',keywords='',hackinfo=''):


        self.env_init(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo)

        return

