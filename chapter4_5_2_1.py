# 4.5. 例外処理(エラーハンドリング)
# 4.5.2. 独自例外
# raise
#raise  IndexError('test Error')

# 独自の例外を作成
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']

    for word in words:
        if word.isupper():
            raise UppercaseError(word)

check()