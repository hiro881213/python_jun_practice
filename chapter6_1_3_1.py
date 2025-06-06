# 6.1. クラスとメソッド
# 6.1.3. オブジェクトの最後に実行される処理を作成する
class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('Good bye')

person = Person('Mike')
print('###########')