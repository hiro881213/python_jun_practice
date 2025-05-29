# 4.4. 変数の有効範囲
# 4.4.2. ローカル変数やグローバル変数を出力する
# ローカル変数を出力する
def f():
    animal = 'dog'
    print('local:', locals())

f()