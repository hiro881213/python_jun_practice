# 3.3. 繰り返し処理
# 3.3.5. for else文の使い方
for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
else:
    print('I ate all.')

# for else文とbreak文
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break

    print(fruit)
else:
    print('I ate all.')