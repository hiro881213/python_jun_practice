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

# 円の面積を求める
# クロージャーの定義
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area