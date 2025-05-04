# 1.2. 文字列のさまざまな操作方法
# 1.2.4. 文字列に他の値を挿入する
# 文字列の挿入
print("a is {}".format("a"))
print("a is {}".format("test"))

# 複数の文字列の挿入
print("a is {} {} {}".format(1,2,3))

# インデックスによる複数の文字列の挿入1
print("a is {0} {1} {2}".format(1,2,3))
print("a is {2} {1} {0}".format(1,2,3))

# インデックスによる複数の文字列の挿入2
print("My name is {0} {1}. Watashi wa {1} {0}.".format("Keanu", "Reeves"))

# インデックスを文字列にする
print("My name is {name} {family}. Watashi wa {family} {name}.".format(name = "Keanu", family = "Reeves"))

# f-string
a = "a"
print(f"a is {a}.")

# f-stringによる複数の文字列の挿入
x, y, z = 1, 2, 3
print(f"a is {x} {y} {z}.")
print(f"a is {z} {y} {x}.")