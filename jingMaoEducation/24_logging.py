import logging

logging.basicConfig(level=logging.INFO,
                    filename='./24_log.txt',
                    filemode='a',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# use logging
logging.info('这是 loggging info message')
logging.debug('这是 loggging debug message')
logging.warning('这是 loggging a warning message')
logging.error('这是 an loggging error message')
logging.critical('这是 loggging critical message')
