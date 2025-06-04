# 6.1. クラスとメソッド
# 6.1.2. クラスが初期化される時の処理
# インスタンス変数
class Person:
    def __init__(self, name):
        self.name = name
        print(self.name)

person = Person('Mike')