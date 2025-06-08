# 6.2. クラスの活用
# 6.2.3. 抽象クラスの使い方
import abc

class Person(metaclass = abc.ABCMeta):
    def __init(self, age = 1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass

