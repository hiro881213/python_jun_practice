# 6.2. クラスの活用
# 6.2.1. プロパティの使い方
# 6.2.1.4. アンダースコア付きの変数を使う時の注意点
class Car:
    def __init__(self, model = None):
        self.model = model

class AdvancedCar(Car):
    def __init__(self, model = 'SUV', enable_auto_run = False):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

advanced_car = AdvancedCar('SUV')
advanced_car.__enable_auto_run = 'XXXXXXXXX'
print(advanced_car.__enable_auto_run)