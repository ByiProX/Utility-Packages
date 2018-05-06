######################################################
# testMyLogging.py
# 此文件要和myLogging文件放在同一目录下
######################################################
from myLogging import MyLogging

if __name__ == '__main__':
    m = MyLogging()
    m.debug('debug')
    m.info('info')
    m.warning('warning')
    m.error('error')
    m.critical('critical')

