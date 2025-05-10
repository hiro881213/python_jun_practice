# 2.1. 複数データを並列にまとめる
# 2.1.5. リストの具体的な利用例
seat =[]
min = 0
max = 5

# 乗客を乗せる
seat.append('p')
print(min <= len(seat) < max)
print(len(seat))

# 乗客が乗れなくなるまで乗せる
seat.append('p')
seat.append('p')
seat.append('p')
seat.append('p')

print(min <= len(seat) < max)
print(len(seat))

# 乗客を下ろす
seat.pop()

print(min <= len(seat) < max)
print(len(seat))