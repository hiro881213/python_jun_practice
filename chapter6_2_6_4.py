# 6.2. クラスの活用
# 6.2.6. クラスメソッドとスタティックメソッド
# 6.2.6.2. スタティックメソッド
class Person:
    @staticmethod
    def about():
        print('about human')

Person.about()