# 4.4. 変数の有効範囲
# 4.4.1. 変数の有効範囲
# 関数内でグローバル変数に値を入れる
anima = 'cat'

def f():
    global animal
    animal = 'dog'
    print('local:', animal)

f()
print('global:', animal)