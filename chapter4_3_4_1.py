# 4.3. 内包表記でリストを生成する
# 4.3.4. ジェネレータ内包表記の書き方
# forループでジェネレータを作成する
def g():
    for i in range(10):
        yield i

g = g()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 内包表記でジェネレータを作成する
g = (i for i in range(10))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
