# 1.2. 文字列のさまざまな操作方法
# 1.2.3. 文字列のメソッドを利用する
s = 'My name is Mike. Hi Mike.'

# startsWithメソッド
is_start1 = s.startswith('My')
is_start2 = s.startswith('X')

print(is_start1)
print(is_start2)

# findメソッド
print(s.find('Mike'))

# rfindメソッド
print(s.rfind('Mike'))

# countメソッド
print(s.count('Mike'))