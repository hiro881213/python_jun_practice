# 4.2. 関数の応用
# 4.2.1. 関数内関数
# 4.2.1.1. 関数内関数の基本
# 関数内関数
def outer(a, b):
    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)

outer(1, 2)