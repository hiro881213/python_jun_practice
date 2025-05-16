# 3.2. 条件分岐
# 3.2.4. 値が入っていないことを判定する
# Boolean型の変数をそのままif文に書く
is_ok = True

if is_ok:
    print('OK!')
else:
    print('No!')

# 変数に数値が入っていた場合のifの判定
is_ok = 1

if is_ok:
    print('OK!')
else:
    print('No!')

# 変数に0が入っていた場合のifの判定
is_ok = 0

if is_ok:
    print('OK!')
else:
    print('No!')

# 変数に数値が入っていた場合のifの判定
is_ok = 10020

if is_ok:
    print('OK!')
else:
    print('No!')

# 変数の文字列に空文字が入っていた場合のifの判定
is_ok = ''

if is_ok:
    print('OK!')
else:
    print('No!')