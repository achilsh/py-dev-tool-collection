import logging
from logging.handlers import RotatingFileHandler

# 创建一个logger
logger = logging.getLogger() ## __name__
logger.setLevel(logging.DEBUG)

# 创建一个RotatingFileHandler，设置文件大小和备份文件个数
file_handler = RotatingFileHandler('my_log.log', maxBytes=100, backupCount=5)
file_handler.setLevel(logging.DEBUG)

# 创建一个StreamHandler，用于在终端输出日志
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# 创建一个Formatter，设置日志格式
formatter = logging.Formatter('%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s')
# formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s:%(lineno)d %(levelname)s %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 将handler添加到logger中
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

