# 4.4. 変数の有効範囲
# 4.4.2. ローカル変数やグローバル変数を出力する
# ローカル変数を出力する
def f():
    animal = 'dog'
    print('local:', locals())

f()

# 空のローカル変数
def f2():
    print('local:', locals())

f2()

# globals関数
animal = 'cat'
print('global:', globals())

