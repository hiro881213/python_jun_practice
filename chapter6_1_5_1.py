# 6.1. クラスとメソッド
# 6.1.5. 継承元のメソッドを上書きして実行する
# 6.1.5.1. メソッドのオーバーライド
class Car:
    def run(self):
        print('run')

class MyCar(Car):
    def run(self):
        print('fast')

class AdvancedCar(Car):
    def run(self):
        print('super fast')

car = Car()
car.run()

print('###############')

my_car = MyCar()
my_car.run()

print('###############')

advanced_car = AdvancedCar()
advanced_car.run()
