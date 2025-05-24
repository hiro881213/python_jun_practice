# 4.1. 関数
# 4.1.3. デフォルト引数でリストや辞書型を使う
def sample_func(x, l = []):
    l.append(x)

    return l

# デフォルト引数に空のリストを使う
y = [1, 2, 3]
r = sample_func(100, y)
print(r)

y = [1, 2, 3]
r = sample_func(200, y)
print(r)

# デフォルト引数に空のリストを複数回呼び出す

r = sample_func(100)
print(r)

r = sample_func(100)
print(r)
