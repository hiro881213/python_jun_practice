# 3.3. 繰り返し処理
# 3.3.9. 辞書をfor文で処理する
# 辞書をfor文で処理する
d = {'x': 100, 'y': 200}

for v in d:
    print(v)

# itemsメソッド
d = {'x': 100, 'y': 200}

for k, v in d.items():
    print(k, ':', v)

# itemsの中身
print(d.items())