# 6.1. クラスとメソッド
# 6.1.2. クラスが初期化される時の処理
# 自分自身のメソッドを呼び出す
class Person:
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)

person = Person('Mike')
person.say_something()