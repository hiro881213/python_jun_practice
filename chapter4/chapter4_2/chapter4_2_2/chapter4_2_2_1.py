# 4.2. 関数の応用
# 4.2.2. デコレータで関数の前後に処理を加える
# デコレータを使わない
def add_num(a, b):
    return a + b

print('start')
r = add_num(10, 20)
print('end')

print(r)

# デコレータの関数を作成する
def print_info(func):
    # wrapper関数
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')

        return result

    return wrapper

# デコレータの実行
f = print_info(add_num)
r = f(10, 20)
print(r)