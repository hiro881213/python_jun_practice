# 3.3. 繰り返し処理
# 3.3.2. while else文
# while else文の基本
count = 0

while count < 5:
    print(count)
    count += 1
else:
    print('Done')

# while else文とbreak文
count = 0

while count < 5:
    if count == 1:
        break

    print(count)
    count += 1
else:
    print('Done')