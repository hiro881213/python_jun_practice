# 3.2. 条件分岐
# 3.2.3. inとnotの利用
# 3.2.3.1. inとnotの基本

y = [1, 2, 3]
x = 1

# in
if x in y:
    print('in')

# not
if 100 not in y:
    print('not in')

# not
a = 1
b = 10

if not a == b:
    print('not equal')