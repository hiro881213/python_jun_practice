# 2.4. データ同士の演算ができる集合
# 2.4.3. 集合の利用
# 共通の友人を求める
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}

print(my_friends & A_friends)

# リスト型に変換して集合にする
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)

print(kind)