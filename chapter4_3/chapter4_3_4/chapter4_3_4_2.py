# 4.3. 内包表記でリストを生成する
# 4.3.4. ジェネレータ内包表記の書き方
# 内包表記でタプルを作成する
g = tuple(i for i in range(10))

print(type(g))
print(g)