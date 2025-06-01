# 4.5. 例外処理(エラーハンドリング)
# 4.5.1. 例外処理
# 4.5.1.3. else
l = [1, 2, 3]
i = 5

try:
    l[0]

except IndexError as ex:
    print("Don't Worry: {}".format(ex))
except NameError as ex:
    print(ex)
else:
    print("done")
finally:
    print("clean up")