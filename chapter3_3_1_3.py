# 3.3. 繰り返し処理
# 3.3.1. while文,continue文,break文の使い方
# 3.3.1.2. continue文
count = 0

while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1