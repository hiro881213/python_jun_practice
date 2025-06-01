# 4.1. 関数
# 4.1.4. 位置引数をタプル化してまとめる
# 引数を渡す際にアンパッキングする
def say_something(word, *args):
    print('word = ', word)

    for arg in args:
        print(arg)

t = ('Mike', 'Nancy')
say_something('Hi!', *t)