# 6.2. クラスの活用
# 6.2.6. クラスメソッドとスタティックメソッド
# 6.2.6.1. クラスメソッド
class Person:
    kind = 'human'

    def __init__(self):
        self.x = 100

a = Person()
print(a)

b = Person
print(b)