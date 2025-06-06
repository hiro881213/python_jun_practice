# 6.1. クラスとメソッド
# 6.1.4. クラスの継承
class Car:
    def run(self):
        print('run')

class AdvancedCar(Car):
    def auto_run(self):
        print('auto run')

advanced_car = AdvancedCar()
advanced_car.run()
advanced_car.auto_run()