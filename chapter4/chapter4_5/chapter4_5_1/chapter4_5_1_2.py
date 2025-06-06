# 4.5. 例外処理(エラーハンドリング)
# 4.5.1. 例外処理
# 4.5.1.2. finally
l = [1, 2, 3]
i = 5
del l

try:
    l[i]
except IndexError as ex:
    print("Don't worry :{}".format(ex))
except NameError as ex:
    print(ex)
finally:
    print("clean up")

# エラー発生をcatchしないパターン
try:
    l[i]
finally:
    print("clean up")