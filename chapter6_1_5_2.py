# 6.1. クラスとメソッド
# 6.1.5. 継承元のメソッドを上書きして実行する
# 6.1.5.2. superで継承元のメソッドを呼び出す
class Car:
    def __init__(self, model = None):
        self.model = model

class MyCar(Car):
    pass

class AdvancedCar(Car):
    pass

my_car = MyCar('sedan')
print(my_car.model)

advanced_car = AdvancedCar('SUV')
print(advanced_car.model)
