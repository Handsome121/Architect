"""
python 日志系统
"""
import logging

# 获取logging对象
logger = logging.getLogger(__name__)
# 增加一个header
header = logging.FileHandler('./demo.log')
# 格式化方式
logger_format = logging.Formatter(
    '%(asctime)s %(created)f %(filename)s %(funcName)s %(levelname)s %(levelno)s %(lineno)d %(message)s')
# 记录日志登记
header.setLevel(logging.INFO)
# 使格式化方式生效
header.setFormatter(logger_format)
# header生效
logger.addHandler(header)
# 打印日志
logger.debug('1111')
logger.error('222')

