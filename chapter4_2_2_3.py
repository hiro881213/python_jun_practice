# 4.2. 関数の応用
# 4.2.2. デコレータで関数の前後に処理を加える
# 複数のデコレータをラップする
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)

        return result

    return wrapper

@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)