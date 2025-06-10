# 6.2. クラスの活用
# 6.2.7. 特殊メソッドの利用
# 6.2.7.3. __add__
class Word:
    def __init__(self, text):
        self.text = text

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

w = Word('TEST')
w2 = Word('#########')
print(w + w2)