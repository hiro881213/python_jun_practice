# 6.2. クラスの活用
# 6.2.4. 多重継承で複数の機能を持ったクラスを作成する
class Person:
    def talk(self):
        print('talk')

class Car:
    def run(self):
        print('run')

class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()