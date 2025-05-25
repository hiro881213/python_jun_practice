# 4.2. 関数の応用
# 4.2.2. デコレータで関数の前後に処理を加える
# デコレータの省略
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')

        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)
