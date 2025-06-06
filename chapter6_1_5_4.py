# 6.1. クラスとメソッド
# 6.1.5. 継承元のメソッドを上書きして実行する
# 6.1.5.2. superで継承元のメソッドを呼び出す
# superの利用
class Car:
    def __init__(self, model = None):
        self.model = model

class AdvancedCar(Car):
    def __init__(self, model = 'SUV', enable_auto_run = False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

advanced_car = AdvancedCar('SUV')
print(advanced_car.model)