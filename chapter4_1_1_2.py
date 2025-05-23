# 4.1. 関数
# 4.1.1.　関数の定義
# 4.1.1.2.　返り値
# 返り値
def say_something2():
    s = 'Hi'
    return s

result = say_something2()
print(result)

def what_is_this(color):
    print(color)

what_is_this('red')

# 引数２
def what_is_this2(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this2('red')
print(result)