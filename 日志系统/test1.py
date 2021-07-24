# import logging
#
# FORMAT = "%(asctime)-15s Thread info: %(thread)d %(threadName)s %(message)s"
# logging.basicConfig(format=FORMAT, level=logging.WARNING)  # 初始化时，如果没指定level，那么level的默认级别为WARNING
# logging.info("打印测试 {}".format(1))  # info不显示
# logging.warning("打印测试 {}".format(2))  # warning是默认级别


# import logging
#
# FORMAT = "%(asctime)-15s Thread info: %(thread)d %(threadName)s %(message)s"
# logging.basicConfig(format=FORMAT,level=logging.INFO) #初始化时，如果没指定level，那么level的默认级别为WARNING
#
# logging.info("我是 {}".format(20)) #单一字符串输出
# logging.info("我是 %d %s",20,"岁") #c风格输出


# 如果需要使用自定义格式，可用在format字符串中指定，在打印字符串时传入extra字典对应即可
# import logging
#
# FORMAT = "%(asctime)-15s Thread info: %(thread)d %(threadName)s %(message)s %(gdy)s %(xdd)s"
# logging.basicConfig(format=FORMAT, level=logging.INFO)  # 初始化时，如果没指定level，那么level的默认级别为WARNING
#
# logging.info("我是 {}".format(20), extra={"xdd": "我是xdd变量", "gdy": "我是gdy变量"})  # 单一字符串输出
# logging.info("我是 %d %s", 20, "岁", extra={"xdd": "我是xdd变量", "gdy": "我是gdy变量"})  # c风格输出


# # 如果输出日期需要了指定格式。可以在basicConfig中使用datefmt参数为日期指定格式
# import logging
#
# logging.basicConfig(format="%(asctime)s %(message)s",datefmt="%Y%m%d %H:%M:%S")
# logging.warning("你好")


# 如果需要将信息输出到文件可以定义filename选择，在basicConfig中
# import logging
#
# logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%Y%m%d %H:%M:%S", filename="./test.log")
#
# for i in range(5):
#     logging.warning("你好 {}".format(i))


# 同时定义多个输出位置,设置handlers
# import logging
# import sys
#
# logging.basicConfig(style="{",
#                     format="{asctime} {name} {message}",
#                     datefmt="%Y-%m-%d %H:%M:%S",
#                     # stream=sys.stdout,
#                     handlers=[logging.StreamHandler(sys.stdout), logging.StreamHandler(sys.stdout),
#                               logging.FileHandler("D:/a.log")],
#                     level=logging.INFO)
# logging.info("aaa %d %s %d", 1, "2", 3)




