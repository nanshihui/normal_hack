# normal_hack
[![Build Status](http://nanshihui.github.io/public/status.svg)](http://nanshihui.github.io/2016/01/21/ToolForSpider%E7%AE%80%E4%BB%8B/) [![Python 2.6|2.7](http://nanshihui.github.io/public/python.svg)](https://www.python.org/) [![License](http://nanshihui.github.io/public/license.svg)](http://nanshihui.github.io/2016/01/21/ToolForSpider%E7%AE%80%E4%BB%8B/) 
　　based on search engine and get the valid infomation to test the vulnerability
### 建立一个通用的漏洞检测框架，使得只要配置上ｐｏｃ就可以直接验证
同时该项目也是toolforspider的从机配置，从机可以直接读取服务器相应的任务执行相应的操作，自己同时也是一个自由的漏洞的检测框架。
##spidertool 爬虫相关工具包
* spidertool    爬虫需要的，常见工具包，以及相关配置
* model     任务实体类(task beans )
* worker 工作实体类

### 注意事项
* 程序入口在worker里面的workerfactory.py
* 需要安装nmap
* PS:if want to help with me to complete this project ...please fork it ^_^  