#!/usr/bin/env python
# encoding: utf-8


class T(object):
    def __init__(self):

        self.result = {
                'type': None,
                'version': None,
                }
        self.keywords = []
        self.versions = []

    def match(self, keyword, server_info):
        if hasattr(keyword, 'search'):
            if keyword.search(server_info):
                return True
        elif isinstance(keyword, basestring):
            keyword = keyword.lower()
            if keyword in server_info:
                return True

    def parse_version(self, server_info):
        for version in self.versions:
            if hasattr(version, 'search'):
                r = version.search(server_info)
                if r:
                    return r.group(1)

    def entry(self, resp, result={}, **kw):# cache={}, result={}, **kw):
        assert self.result['type']
        if resp.history:
            headers = dict(resp.history[0].headers)
        else:
            headers = dict(resp.headers)
        server_info = headers.get('server', '').lower()
        for keyword in self.keywords:
            r = self.match(keyword, server_info)
            if not r:
                continue
            r = self.parse_version(server_info)
            if r:
                self.result['version'] = r
            return self.result

    def verify(self):
        
        
        pass
    def attack(self):
        
        pass
    def parse_output(self, result):
        
        pass