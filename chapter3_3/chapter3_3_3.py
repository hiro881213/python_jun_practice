# 3.3. 繰り返し処理
# 3.3.3. input関数
while True:
    word = input('Enter:')

    if word == 'ok':
        break

    print('next')

# input関数と数値
while True:
    word = input('Enter:')
    num = int(word)

    if num == 100:
        break

    print('next')