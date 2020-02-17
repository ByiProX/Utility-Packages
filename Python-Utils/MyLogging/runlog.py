# -*- coding:utf-8 -*-
import logging.config
import time

import yaml

with open('./conf/runlog.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger("Prod")

if __name__ == '__main__':
    while True:
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        time.sleep(5)

