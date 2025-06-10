# 6.2. クラスの活用
# 6.2.7. 特殊メソッドの利用
# 6.2.7.4. __eq__
# __eq__メソッドの利用
class Word:
    def __init__(self, text):
        self.text = text

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('test')
w2 = Word('test')

print(w == w2)