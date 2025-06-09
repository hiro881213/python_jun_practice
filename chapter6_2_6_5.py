# 6.2. クラスの活用
# 6.2.6. クラスメソッドとスタティックメソッド
# 6.2.6.2. スタティックメソッド
class Person:
    @staticmethod
    def about(year):
        print('about human {}'.format(year))

Person.about(1999)