# 3.3. 繰り返し処理
# 3.3.4. for文の使い方
some_list = [1, 2, 3, 4, 5]

# while文でリストの要素を取り出す
i = 0

while i < len(some_list):
    print(some_list[i])
    i += 1

# for文でリストの要素を取り出す
for i in some_list:
    print(i)

# for文で文字列を取り出す
for s in 'abcde':
    print(s)

# for文で文字列のリストを取り出す
for word in ['My', 'name', 'is', 'Mike']:
    print(word)

# for文とbreak文
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        break

    print(word)