# 4.3. 内包表記でリストを生成する
# 4.3.2. 辞書包括表記の書き方
# 辞書包括表記を使わないパターン
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)