# 1.1.1. 変数の宣言
# 数値の宣言
num = 1
print(num)

# 文字列の宣言
name = 'Mike'
print(name)

# type関数
print(type(num))
print(type(name))

# Boolean型
is_ok = True
print(is_ok)
print(type(is_ok))

#変数に違う型の値を入れる
num2 = 2
name2 = 'Mike'
num2 = name2

print(num2, type(num2))

#型の変換
name3 = '3'
new_num = int(name3)

print(new_num, type(new_num))

#型の宣言
num4: int = 1
name4: str = '1'
num4 = name4

print(num4, type(num4))