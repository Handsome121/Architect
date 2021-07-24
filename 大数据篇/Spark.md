# Spark

Apache Spark 是专为大规模[数据处理](https://baike.baidu.com/item/数据处理/944504)而设计的快速通用的计算引擎。Spark是UC Berkeley AMP lab ([加州大学伯克利分校](https://baike.baidu.com/item/加州大学伯克利分校/3755024)的AMP实验室)所开源的类Hadoop MapReduce的通用并行框架，Spark，拥有Hadoop MapReduce所具有的优点；但不同于MapReduce的是——Job中间输出结果可以保存在内存中，从而不再需要读写HDFS，因此Spark能更好地适用于数据挖掘与机器学习等需要迭代的MapReduce的算法。

Spark 是一种与 Hadoop 相似的开源集群计算环境，但是两者之间还存在一些不同之处，这些有用的不同之处使 Spark 在某些工作负载方面表现得更加优越，换句话说，Spark 启用了内存分布数据集，除了能够提供交互式查询外，它还可以优化迭代工作负载。

Spark 是在 Scala 语言中实现的，它将 Scala 用作其应用程序框架。与 Hadoop 不同，Spark 和 [Scala](https://baike.baidu.com/item/Scala/2462287) 能够紧密集成，其中的 Scala 可以像操作本地集合对象一样轻松地操作分布式数据集。

尽管创建 Spark 是为了支持分布式数据集上的[迭代](https://baike.baidu.com/item/迭代/8415523)作业，但是实际上它是对 Hadoop 的补充，可以在 Hadoop 文件系统中并行运行。通过名为 Mesos 的第三方集群框架可以支持此行为。Spark 由加州大学伯克利分校 AMP 实验室 (Algorithms, Machines, and People Lab) 开发，可用来构建大型的、低延迟的数据分析应用程序。

#### 基本介绍

 Apache Spark是专为大规模数据处理而设计的快速通用的计算引擎 [2] 。现在形成一个高速发展应用广泛的生态系统。 

#### 特点

Spark 主要有三个特点 ：

首先，高级 API 剥离了对集群本身的关注，Spark 应用开发者可以专注于应用所要做的计算本身。

其次，Spark 很快，支持交互式计算和复杂算法。

最后，Spark 是一个通用引擎，可用它来完成各种各样的运算，包括 SQL 查询、文本处理、机器学习等，而在 Spark 出现之前，我们一般需要学习各种各样的引擎来分别处理这些需求。

#### 性能特点

- 更快的速度

内存计算下，Spark 比 Hadoop 快100倍。

- 易用性

Spark 提供了80多个高级运算符。

- 通用性

Spark 提供了大量的库，包括Spark Core、Spark SQL、Spark Streaming、MLlib、GraphX。 开发者可以在同一个应用程序中无缝组合使用这些库。

- 支持多种资源管理器

Spark 支持 Hadoop YARN，Apache Mesos，及其自带的独立集群管理器

- Spark生态系统
- Shark：Shark基本上就是在Spark的框架基础上提供和Hive一样的HiveQL命令接口，为了最大程度的保持和Hive的兼容性，Spark使用了Hive的API来实现query Parsing和 Logic Plan generation，最后的PhysicalPlan execution阶段用Spark代替HadoopMapReduce。通过配置Shark参数，Shark可以自动在内存中缓存特定的RDD，实现数据重用，进而加快特定数据集的检索。同时，Shark通过UDF用户自定义函数实现特定的数据分析学习算法，使得SQL数据查询和运算分析能结合在一起，最大化RDD的重复使用。
- SparkR：SparkR是一个为R提供了轻量级的Spark前端的R包。 SparkR提供了一个分布式的data frame数据结构，解决了 R中的data frame只能在单机中使用的瓶颈，它和R中的data frame 一样支持许多操作，比如select,filter,aggregate等等。（类似dplyr包中的功能）这很好的解决了R的大数据级瓶颈问题。 SparkR也支持分布式的机器学习算法，比如使用MLib机器学习库。 [4] SparkR为Spark引入了R语言社区的活力，吸引了大量的数据科学家开始在Spark平台上直接开始数据分析之旅。

#### 基本原理

 Spark Streaming：构建在Spark上处理Stream数据的框架，基本的原理是将Stream数据分成小的时间片段（几秒），以类似batch批量处理的方式来处理这小部分数据。Spark Streaming构建在Spark上，一方面是因为Spark的低延迟执行引擎（100ms+），虽然比不上专门的流式数据处理软件，也可以用于实时计算，另一方面相比基于Record的其它处理框架（如Storm），一部分窄依赖的RDD数据集可以从源数据重新计算达到容错处理目的。此外小批量处理的方式使得它可以同时兼容批量和实时数据处理的逻辑和算法。方便了一些需要历史数据和实时数据联合分析的特定应用场合。





#### 目标 

- 架构及生态
- spark 与 hadoop
- 运行流程及特点
- 常用术语
- standalone模式
- yarn集群
- RDD运行流程

