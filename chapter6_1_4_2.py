# 6.1. クラスとメソッド
# 6.1.4. クラスの継承
class Car:
    def run(self):
        print('run')

class MyCar(Car):
    pass

car = Car()
car.run()

my_car = MyCar()
my_car.run()