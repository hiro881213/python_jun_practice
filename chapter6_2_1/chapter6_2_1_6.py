# 6.2. クラスの活用
# 6.2.1. プロパティの使い方
# 6.2.1.3. 変数にアンダースコアをつける
class Car:
    def __init__(self, model = None):
        self.model = model

class AdvancedCar(Car):
    def __init__(self, model = 'SUV', enable_auto_run = False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

advanced_car = AdvancedCar('SUV')
print(advanced_car._enable_auto_run)