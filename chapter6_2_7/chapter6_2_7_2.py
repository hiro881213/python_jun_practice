# 6.2. クラスの活用
# 6.2.7. 特殊メソッドの利用
# 6.2.7.2. __len__
class Word:
    def __init__(self, text):
        self.text = text

    def __len__(self):
        return len(self.text)

w = Word('test')
print(len(w))
