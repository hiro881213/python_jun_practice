# 2.3. 辞書型
# 2.3.3. 辞書のコピー
# 辞書型の参照渡し
x = {'a': 1}
y = x
y['a'] = 1000

print(x)
print(y)

# copyメソッド
x = {'a': 1}
y = x.copy()
y['a'] = 1000

print(x)
print(y)