# 2.4. データ同士の演算ができる集合
# 2.4.1. 集合型の基本
# 集合の作成
a = {1, 2, 2, 3, 4, 4, 5, 6}

print(a)
print(type(a))

# 集合の差
b = {2, 3, 3, 6, 7}
print(a - b)
print(b - a)

# 集合の積
print(a & b)

# 集合の和
print(a | b)

# 集合の対称差
print(a ^ b)