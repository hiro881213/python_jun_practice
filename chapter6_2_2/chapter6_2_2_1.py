# 6.2. クラスの活用
# 6.2.2. 例外とダックタイピング
class Car:
    def ride(self, person):
        person.drive()

class Person:
    def __init__(self, age = 1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')

class Baby(Person):
    def __init__(self, age = 1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age = 18):
        if age >= 18:
            super().__init__(age)
        else: raise ValueError
