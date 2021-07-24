# Python中的logging日志输出模块

#### 日志级别

| 日志级别Level | 对应数值    |
| ------------- | ----------- |
| CRITICAL      | 50          |
| ERROR         | 40          |
| WARRNING      | 30,默认级别 |
| INFO          | 20          |
| DEBUG         | 10          |
| NOTSET        | 0           |

日志级别指的是产生日志的事件的严重程度。
设置一个级别后，严重程度低于设置的日志消息将被忽略。
对应的打印方法有：debug()、info()、warning()、error()、和critical()方法 

#### 常用的格式字符串

| 属性名称     | 格式            | 描述                                                         |
| ------------ | --------------- | ------------------------------------------------------------ |
| 日志消息内容 | %(message)s     | 使用对应级别打印时传入的message变量值。 可以使用Formatter.format()设置设置打印格式。 |
| asctime      | %(asctime)s     | 创建LogRecord时的可读时间。默认情况下，它的格式为’2003-07-08 16:49:45,896’（逗号后面的数字是毫秒部分的时间） |
| 函数名       | %(funcName)s    | 日志调用所在函数的函数名                                     |
| logger名称   | %(name)s        | logger的名字                                                 |
| 日志级别名称 | %(levelname)s   | 消息的级别名称： “DEBUG”,“INFO”,“WARNING”,“ERROR”,“CRITICAL” |
| 日志级别数值 | %(levelno)s     | 消息的级别数字，对应DEBUG,INFO,WARNING,ERROR,CRITICAL        |
| 行号         | %(lineno)d      | 日志调用所在的源码行号                                       |
| 模块         | %(module)d      | 模块(filename名字部分)                                       |
| 进程ID       | %(process)d     | 进程ID                                                       |
| 线程ID       | %(thread)d      | 线程ID                                                       |
| 进程名称     | %(processName)s | 进程名称                                                     |
| 线程名称     | %(threadName)s  | 线程名称                                                     |
| logger名称   | %(name)s        | 使用的logger对应名称                                         |
| pathname     | %(pathname)s    | 输出日志调用的文件完整路径                                   |

注意：funcName,threadName,processName都是小驼峰。

#### logging.basicConfig参数解析

- logging.basicConfig(**kwargs)
- logging.basicConfig会初始化配置logging.root日志输出模块的配置信息。

| 关键字参数名称 | 意思                                                         |
| -------------- | ------------------------------------------------------------ |
| filename       | 类型(字符串)，定义模块输出的日志在指定文件中。不能与stream同时指定。 如果不指定默认使用sys.stderr流对象输入，即标准错误输出。 |
| filemode       | 如果指定了filename，那么打开文件的模式为filemode模式，默认为“a”模式打开。 |
| stream         | 指定日志文件输出的流对象，默认为sys.stderr流对象，不能与filename同时存在，会触发ValueError异常。 |
| format         | 为处理程序指定格式化字符串，默认为：`%(levelname)s:%(name)s:%(message)s` |
| datefmt        | 使用指定日期时间的格式time.strftime()                        |
| style          | 指定默认字符串使用的格式。注意：info等打印日志时传入的参数只能使用c风格，即“%”风格。可选择值如下： "%":表示使用c风格格式字符串,此时默认的format格式为："%(levelname)s:%(name)s:%(message)s"。 "{"：表示使用format,此时format格式为："{levelname}:{name}:{message}"。 "&quot; : 使 用 S t r i n g T e m p l a t e S t y l e 风 格 。 此 时 f o r m a t 格 式 为 ： &quot; l e v e l n a m e : &quot;:使用StringTemplateStyle风格。此时format格式为：&quot;{levelname}:":使用*S**t**r**i**n**g**T**e**m**p**l**a**t**e**S**t**y**l**e*风格。此时*f**o**r**m**a**t*格式为："*l**e**v**e**l**n**a**m**e*:{name}?{message}" |
| level          | 设置root日志输出的级别                                       |
| handlers       | 添加其他输出日志方式，实际输出日志都是handler的作用。如果设置了handlers列表，那么同时不能使用filename和stream参数，否则会抛出ValueError异常。 |