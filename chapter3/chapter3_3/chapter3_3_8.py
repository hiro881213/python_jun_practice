# 3.3. 繰り返し処理
# 3.3.8. zip関数
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee','tea', 'beer']

# zip関数を使わない
for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

# zip関数
for day,  fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)