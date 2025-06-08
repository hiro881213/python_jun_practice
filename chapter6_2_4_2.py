# 6.2. クラスの活用
# 6.2.4. 多重継承で複数の機能を持ったクラスを作成する
# 多重継承の順番
class Person:
    def talk(self):
        print('talk')

    def run(self):
        print('person run')

class Car:
    def run(self):
        print('car run')

class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.run()