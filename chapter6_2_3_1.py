# 6.2. クラスの活用
# 6.2.3. 抽象クラスの使い方
class Person:
    def __init__(self, age = 1):
        self.age = age

class Baby(Person):
    def __init__(self, age = 1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No Drive')

class Adult(Person):
    def __init__(self, age = 18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('ok')