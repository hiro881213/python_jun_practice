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