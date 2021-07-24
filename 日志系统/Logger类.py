# 在logging模块中，顶层代码中有
# root = RootLogger(WARNING) #大约在1824行 指定根Logger对象的默认级别，就在basicConfig函数上面
# Logger.root = root #为类Logger增加类属性root
# Logger.manager = Manager(Logger.root)


# logging模块在加载的时候，就会创建一个全局对象root,它是一个RootLogger示例。根Logger对象的默认级别是WARNING.
# RootLogger类继承自Logger类
# 类Logger初始化方法签名是(name,level=0)
# 类RootLogger初始化方法签名是(name,level=0)
# 类RootLogger初始化方法签名(level),本质上调用的是Logger.__init__(self,"root",WARNING)
# 调用logging.basicConfig来调整级别，就是对这个根Logger的级别进行修改。

# 1、Logger.getLogger函数，构造一个log类
# Logger示例的构建，使用Logger类也行，但推荐使用getLogger函数

# root = RootLogger(WARNING)  #大约在1824行
# Logger.root = root
# Logger.manager = Manager(Logger.root)
#
# def getLogger(name=None):   #大约在1930行
#     """
#     Return a logger with the specified name, creating it if necessary.
#
#     If no name is specified, return the root logger.
#     """
#     if name:
#         return Logger.manager.getLogger(name)
#     else:
#         return root #如果没有指定名称，就返回根logger

# getLogger方法如果没有指定名称，使用工厂方法返回了同一个实例对象。
# 指定了name，返回一个名称为name的Logger实例，如果再次使用相同的名字，会返回同一个实例，不会重新创建新的实例。(背后使用了一个字典保证了同一名字返回同一个Logger实例，具体可继续阅读源码)

# 2、层次结构
# Logger是层次结构的，使用"."点号分割，例如：“a”,"a.b"或者“a.b.c.d”,a是a.b的父parent,a.b是a的子child。对于foo来说，名字为foo.bar、foo.bar.baz、foo.bam都是foo的后代

# import logging
# # 父子层次关系
# # 根logger
# root = logging.root
# print(root, id(root))
# print(root.name, type(root), root.parent)  # 根logger没有父
#
# log1 = logging.getLogger(__name__)  # 模块级别logger
# print(log1.name, type(log1), id(log1), id(log1.parent), log1.parent.name)
#
# log2 = logging.getLogger("{}.{}".format(__name__, "child"))  # 子logger
# print(log2.name, type(log2), id(log2), id(log2.parent), log2.parent.name)

# Level级别设置与level的继承
# 每一个logger实例都有级别，即每个logger实例都有一个等效的level.

# logger对象可以在创建后动态的修改自己的level。

# 等效level决定着logger实例能输出什么级别的信息。

# 如果logger没有设置自己的级别，会默认从依次从父类开始寻找对应的级别，找到后会记录当前级别的信息是否能输出，记录在self._cache字典中

# INFO级别消息示例(部分源码解析)：
# def info(self, msg, *args, **kwargs):
#     if self.isEnabledFor(INFO):  # 先要判断当前级别是否能输出 大约在1373行
#         self._log(INFO, msg, args, **kwargs)


#############################x下面大约在1619行#############################################
# def isEnabledFor(self, level):
"""
Is this logger enabled for level 'level'?
"""
# try:
#     return self._cache[level]
# except KeyError:
#     _acquireLock()
#     if self.manager.disable >= level:  # 注意self.manager记录的是root日志对象，通常情况下是0>=INFO
#         is_enabled = self._cache[level] = False
#     else:  # getEffectiveLevel会获取最近父类的级别，判断是否大于当前INFO的级别如果大于就返回True表示可以输出
#         is_enabled = self._cache[level] = level >= self.getEffectiveLevel()
#     _releaseLock()
#
#     return is_enabled


####################################下面大约在1605行##############################################
# def getEffectiveLevel(self):
#     """
#     Get the effective level for this logger.
#
#     Loop through this logger and its parents in the logger hierarchy,
#     looking for a non-zero logging level. Return the first one found.
#     """
#     logger = self
#     while logger:
#         if logger.level:
#             return logger.level
#         logger = logger.parent
#     return NOTSET
# 如果不设置level，则初始level为0
#
# 如果设置了level，就有限使用自己的level，否则继承最近祖先的level
#
# 信息是否能通过该logger实例上输出，就是要看当前函数的level是否大于等于logger的有效level，否则输出不了。

# 简单示例：
# import logging
# import sys
#
# logging.basicConfig(level=logging.WARNING,
#                     stream=sys.stdout,
#                     format="%(asctime)s %(thread)d %(threadName)s %(name)s [%(message)s]")
#
# logging.warning("warning->我是root")
# logging.info("info->我是root") #不能被输出root默认级别是30，而info级别是20
#
# log1 = logging.getLogger(__name__)
# log1.level = logging.INFO
# log1.info("info->我是log1")
# log1.debug("debug->我是log1")
#
# log2 = logging.getLogger("{}.{}".format(__name__,"log2"))
# # log2.level = logging.DEBUG
# log2.info("info->我是__main__.log2")
# log2.debug("debug->我是__main__.log2") #不能输出，应为log1的级别为INFO=20而DEBUG的输出级别是10，没有达到输出级别

# Handler负责输出信息
# Handler控制日志信息的输出目的地，可以是控制台、文件。 日志输出是Handler做的，也就是真正干活的是Handler。
#
# 可以单独设置level
# 可以单独设置格式Formatter
# 可以设置过滤器Filter
# Handler类的层次
# Handler
# StreamHandler #不指定使用sys.stderr
# FileHandler 文件
# _StderrHandler #标准输出
# NullHandler #什么都不做
# 在logging.basicConfig函数中，如下：

# if handlers is None:
#     filename = kwargs.pop("filename", None)
#     mode = kwargs.pop("filemode", 'a')
#     if filename:
#         h = FileHandler(filename, mode)
#     else:
#         stream = kwargs.pop("stream", None)
#         h = StreamHandler(stream)
#     handlers = [h]
# 如果设置文件名，则为根Logger加载一个输出到文件的FileHandler。
# 如果没有设置文件名，则根Logger加载一个StreamHandler,默认输出到sys.stderr。
# 也就是说根logger一定会至少有一个handler。



# Formatter日志格式类
# logging的Formatter类，它允许指定某个格式的字符串。如果提供None，那么"%(message)s"将会作为默认值。
# Formatter是绑定在Handler上的

# import logging
# import sys
#
# logging.basicConfig(level=logging.WARNING,
#                     stream=sys.stdout,
#                     format="%(asctime)s %(thread)d %(threadName)s %(name)s [%(message)s]")
#
# log1 = logging.getLogger("log1")
# log1.setLevel(logging.INFO)
# print(log1.name,type(log1))
# log1.info("我是log1")
#
# print(" -"* 30)
# filehand = logging.FileHandler("D:/a.log","w") #输出到文件
# log1.addHandler(filehand)
# stdhand1 = logging.StreamHandler(sys.stdout) #输出到标准输出
# fmt = logging.Formatter("%(asctime)s %(name)s [%(message)s]") #为stdhand1单独设置输出格式，如果不设置会默认使用"%(message)s"格式
# stdhand1.setFormatter(fmt)
# log1.addHandler(stdhand1)
# log1.propagate = False #阻止传递
# log1.info("你好")
#
# print("- "*30)
# log2 = logging.getLogger("log2")
# log2.setLevel(logging.INFO)
# print(log2.name,type(log2))
# log2.addHandler(logging.StreamHandler(sys.stdout))
# log2.addHandler(logging.StreamHandler(sys.stdout))
# print(log2.propagate)
# log2.info("我是log2") #不会阻止传播


