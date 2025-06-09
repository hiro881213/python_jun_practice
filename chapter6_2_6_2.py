# 6.2. クラスの活用
# 6.2.6. クラスメソッドとスタティックメソッド
# 6.2.6.1. クラスメソッド
class Person:
    kind = 'human'

    def __init__(self):
        self.x = 100

    def what_is_your_kind(self):
        return self.kind

a = Person()
print(a.what_is_your_kind())