#!/usr/bin/env python
# encoding: utf-8


from os.path import dirname, abspath, join, isdir
from os import listdir
from urlparse import urljoin
from re import compile



title_regex = compile('<title[^<>]*>([\s\S]*?)<\\?/title>', 2)
meta_regex = compile('<meta\s+[^<>]*?content=["\']([^"\']*?)["\']', 2)

class PocController(object):
    def __init__(self, site=None, resp=None,  result={}, suffixes=[], request=None, logger=None):
        self.modules_list = [

                {'module_name': 'component',  'resp': resp, 'result': result, 'traverse': True},
 ]
        self.site        = site

        self.result      = result
        self.keywords    = {}
        self.components     = {}
        self.request     = request
        self.logger      = logger

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
#         if __name__ in ('__init__', '__main__'):
#             plugin_name = '%s.%s' % (module_name, plugin_name)
#         else:
#             plugin_name = '%s.%s.%s' % (__name__, module_name, plugin_name)

        plugin_name = '%s.%s' % (module_name, plugin_name)

        plugin = __import__(plugin_name,globals=globals(), fromlist=['P'])

        self.logger.info('Load Plugin: %s.P', plugin_name)

        self.logger and self.logger.info('Load Plugin: %s.P', plugin_name)
        print str(plugin_name)
        return plugin.P
    def __load_keywords(self,componentname, module_name):
        module_name = '%s.'+componentname+'.%s' % (__name__, module_name)
        module = __import__(module_name, fromlist=['KEYWORDS'])
        return module.KEYWORDS
    def __load_component_detail_plugins(self, componentname=''):

        modules_list = self.__get_component_detail_list(componentname)
        for module_name in modules_list:
            self.components[componentname][module_name] = []
            for plugin_name in self.__get_component_plugins_list(componentname,module_name):
                
                P = self.__load(componentname+'.%s' % module_name, plugin_name)
                self.components[componentname][module_name].append(P)
                try:
                    self.keywords[module_name] = self.__load_keywords(componentname,module_name)
                    self.logger and self.logger.info('Module Keywords: %s -> %s', module_name, self.keywords[module_name])
                except:
                    self.keywords[module_name] = []
                    self.logger and self.logger.info('Module Keywords: %s -> None', module_name)
                    pass
    def __load_component_plugins(self, modules_list):
        for module_name in modules_list:
            self.components[module_name] = {}
            self.__load_component_detail_plugins(module_name)

    def loader(self):
        self.components = {}
        self.__load_component_plugins(map(lambda module_info: module_info['module_name'], self.modules_list))

    def detect(self, site, resp, roots=[], mode=0):
        self.mode = mode
        self.loader()
#         self.env_detect(self.modules_list)
# 
# 
# 
#         self.__detect(resp)
        return

