# 4.1. 関数
# 4.1.3. デフォルト引数でリストや辞書型を使う
# デフォルト引数に空のリストを使いたい場合
def sample_func(x, l = None):
    if l is None:
        l = []

    l.append(x)
    return l

r = sample_func(100)
print(r)

r = sample_func(100)
print(r)