# 3.2. 条件分岐
# 3.2.1. if文、else文、elif文の使い方
# 3.2.1.3. elif文
x = 0
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

# 複数のelif文
x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10')
else:
    print('positive')