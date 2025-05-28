# 4.2. 関数の応用
# 4.2.4. ジェネレータ
# ジェネレータを使わない
l = ['Good Morning', 'Good After noon', 'Good night']

for i in l:
    print(i)

# yield
def greeting():
    yield 'Good Morning'
    yield 'Good Afternoon'
    yield 'Good night'

for g in greeting():
    print(g)