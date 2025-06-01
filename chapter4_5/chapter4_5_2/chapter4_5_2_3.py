# 4.5. 例外処理(エラーハンドリング)
# 4.5.2. 独自例外
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']

    for word in words:
        if word.isupper():
            raise UppercaseError(word)

# 独自の例外をexceptで実行
try:
    check()
except UppercaseError as ex:
    print('This is my fault. Go next')