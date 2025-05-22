# 4.1. 関数
# 4.1.1.　関数の定義
# 4.1.1.1.　関数
# 関数定義
def say_something():
    print('Hi')

say_something()

# 関数の呼び出し
say_something

# 変数を関数に入れる
f = say_something
f()

# 返り値
def say_something2():
    s = 'Hi'
    return s

result = say_something2()
print(result)