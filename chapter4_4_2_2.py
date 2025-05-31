# 4.4. 変数の有効範囲
# 4.4.2. ローカル変数やグローバル変数を出力する
# __name__や__doc__を出力する
animal = 'cat'

def f():
    """ Test func doc """
    print(f.__name__)
    print(f.__doc__)

f()
print('global:', __name__)