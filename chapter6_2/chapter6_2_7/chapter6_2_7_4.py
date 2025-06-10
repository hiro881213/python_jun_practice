# 6.2. クラスの活用
# 6.2.7. 特殊メソッドの利用
# 6.2.7.4. __eq__
# __eq__メソッドを使わない
class Word:
    def __init__(self, text):
        self.text = text

w = Word('test')
w2 = Word('test')

print(w == w2)
print(id(w))
print(id(w2))