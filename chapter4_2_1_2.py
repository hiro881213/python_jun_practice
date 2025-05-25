# 4.2. 関数の応用
# 4.2.1. 関数内関数
# 4.2.1.1. 関数内関数とクロージャー
# クロージャー
def outer(a, b):
    def inner():
        return a + b

    return inner

print(outer(1, 2))

f = outer(1, 2)
r = f()
print(r)