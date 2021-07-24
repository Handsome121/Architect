"""
在什么情况下应当使用抽象工厂模式
　一个系统不应当依赖于产品类实例如何被创建、组合和表达的细节，这对于所有形态的工厂模式都是重要的。
　这个系统的产品有多于一个的产品族，而系统只消费其中某一族的产品。
　同属于同一个产品族的产品是在一起使用的，这一约束必须在系统的设计中体现出来。（比如：Intel主板必须使用Intel CPU、Intel芯片组）
　系统提供一个产品类的库，所有的产品以同样的接口出现，从而使客户端不依赖于实现。
"""


class AbstractFactory:
    computer_name = ''

    def createCpu(self):
        pass

    def createMainboard(self):
        pass


class IntelFactory(AbstractFactory):
    computer_name = 'Intel I7-series computer '

    def createCpu(self):
        return IntelCpu('I7-6500')

    def createMainboard(self):
        return IntelMainBoard('Intel-6000')


class AmdFactory(AbstractFactory):
    computer_name = 'Amd 4 computer '

    def createCpu(self):
        return AmdCpu('amd444')

    def createMainboard(self):
        return AmdMainBoard('AMD-4000')


class AbstractCpu(object):
    series_name = ''
    instructions = ''
    arch = ''


class IntelCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series


class AmdCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series


class AbstractMainboard(object):
    series_name = ''


class IntelMainBoard(AbstractMainboard):
    def __init__(self, series):
        self.series_name = series


class AmdMainBoard(AbstractMainboard):
    def __init__(self, series):
        self.series_name = series


class ComputerEngineer(object):

    def makeComputer(self, factory_obj):
        self.prepareHardwares(factory_obj)

    def prepareHardwares(self, factory_obj):
        self.cpu = factory_obj.createCpu()
        self.mainboard = factory_obj.createMainboard()

        info = '''------- computer [%s] info:
    cpu: %s
    mainboard: %s
 -------- End --------
        ''' % (factory_obj.computer_name, self.cpu.series_name, self.mainboard.series_name)
        print(info)


if __name__ == "__main__":
    engineer = ComputerEngineer()

    intel_factory = IntelFactory()

    engineer.makeComputer(intel_factory)

    amd_factory = AmdFactory()
    engineer.makeComputer(amd_factory)
