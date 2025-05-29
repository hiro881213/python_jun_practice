# 4.4. 変数の有効範囲
# 4.4.1. 変数の有効範囲
# グローバル変数
animal = 'cat'
print(animal)

# 関数内からグローバル変数を呼び出す
def f():
    print(animal)

f()

# ローカル変数
animal = 'cat'

def f():
    print(animal)
    animal = 'dog'
    print('after:', animal)

f()