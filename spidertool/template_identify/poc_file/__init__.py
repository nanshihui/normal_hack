from plugins import default

from lib.logger import initLog
if __name__ == '__main__':

    logger = initLog('WebDect.log', 2, True)
    a=default.PocController(logger=logger)
    a.detect(site=None, resp=None, roots=None, mode=None) 
