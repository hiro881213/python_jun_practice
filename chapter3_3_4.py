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