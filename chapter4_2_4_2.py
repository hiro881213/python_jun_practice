# 4.2. 関数の応用
# 4.2.4. ジェネレータ
# 別の一例
def counter(num = 10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good mornig'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
c = counter()

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))