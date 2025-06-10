# 6.2. クラスの活用
# 6.2.1. プロパティの使い方
# 6.2.1.2. セッター
# セッターの使用
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

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

advanced_car = AdvancedCar('SUV')
advanced_car.enable_auto_run = True

print(advanced_car.enable_auto_run)