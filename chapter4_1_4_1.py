# 4.1. 関数
# 4.1.4. 位置引数をタプル化してまとめる
# 複数の引数
def say_something(word, word2, word3):
    print(word)
    print(word2)
    print(word3)

say_something('Hi!', 'Mike', 'Nancy')

# 位置引数のタプル化
def say_something2(*args):
    print(args)

say_something2('Hi!', 'Mike', 'Nancy')

# タプル化した関数で引数を一括処理できるようにする
def say_something3(*args):
    for arg in args:
        print(arg)

say_something3('Hi!', 'Mike', 'Nancy')