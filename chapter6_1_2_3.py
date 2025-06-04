# 6.1. クラスとメソッド
# 6.1.2. クラスが初期化される時の処理
# デフォルト引数を指定する
class Person():
    def __init__(self, name = 'Default'):
        self.name = name
        print(self.name)

person = Person()