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
        result = func(*args, **kwargs)