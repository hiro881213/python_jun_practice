# 4.5. 例外処理(エラーハンドリング)
# 4.5.2. 独自例外
# 既存の例外を発生させる
def check():
    words = ['APPLE', 'orange', 'banana']

    for word in words:
        if word.isupper():
            raise ValueError(word)

try:
    check()
except ValueError as exc:
    print('This is my fault. Go next')