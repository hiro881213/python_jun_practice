# 6.2. クラスの活用
# 6.2.7. 特殊メソッドの利用
# 6.2.7.1. __str__
class Word:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'word!!!!!!!!'

w = Word('test')
print(w)