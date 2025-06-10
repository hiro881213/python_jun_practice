# 6.2. クラスの活用
# 6.2.6. クラスメソッドとスタティックメソッド
# 6.2.6.1. クラスメソッド
class Person:
    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

a = Person()
print(a.what_is_your_kind())

b = Person
print(b.what_is_your_kind())