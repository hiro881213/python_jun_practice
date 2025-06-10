# 6.2. クラスの活用
# 6.2.5. クラス変数で値を共有する
# オブジェクト間で共有するインスタンス変数
class Person:
    def __init__(self, name):
        self.kind = 'human'
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()

b = Person('B')
b.who_are_you()