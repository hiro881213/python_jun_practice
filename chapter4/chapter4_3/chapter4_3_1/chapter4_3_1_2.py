# 4.3. 内包表記でリストを生成する
# 4.3.1. リスト内包表示の書き方
# 4.3.1.2. 2つのforループのリスト内包表記
# リスト内包表記を使わない
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

# リスト内包表記を使う
r = [i * j for i in t for j in t2]
print(r)