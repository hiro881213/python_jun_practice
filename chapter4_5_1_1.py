# 4.5. 例外処理(エラーハンドリング)
# 4.5.1. 例外処理
# 4.5.1.1. 例外処理の基本
# try-except文
l = [1, 2, 3]
i = 5

try:
    l[i]
except:
    print("Don't worry")

# 特定のエラーが発生した場合、処理する
try:
    l[i]
except IndexError:
    print("Don't worry")

# エラーの内容を表示
try:
    l[i]
except IndexError as ex:
    print("Don't Worry: {}".format(ex))