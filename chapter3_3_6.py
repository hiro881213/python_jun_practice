# 3.3. 繰り返し処理
# 3.3.5. range関数

# range関数を使わないパターン
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('###############')
for i in num_list:
    print(i)

# range関数を利用するパターン
print('###############')
for i in range(10):
    print(i)

# range関数で始まりと終わりを指定する
print('###############')
for i in range(2, 10):
    print(i)

# 3ずつ増えるように取り出す
print('###############')
for i in range(2, 10, 3):
    print(i)