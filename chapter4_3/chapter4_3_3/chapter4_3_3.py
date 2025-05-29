# 4.3. 内包表記でリストを生成する
# 4.3.3. 集合内包表記
# 集合内包表記を使わない場合
s = set()

for i in range(10):
    s.add(i)

print(s)

# 集合内包表記を使う場合
s = {i for i in range(10)}
print(s)

# if文を使った集合
s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

# if文と集合内包表記を使う場合
s = { i for i in range(10) if i % 2 == 0 }
print(s)