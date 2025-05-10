# 2.1. 複数データを並列にまとめる
# 2.1.4. リストのコピー
# 2.1.4.2. 値渡しと参照渡し
# 値渡し
X = 20
Y = X
Y = 5

print(id(X))
print(id(Y))
print(X)
print(Y)

# 参照渡し
A = ['a', 'b']
B= A

print(id(A))
print(id(B))
print(A)
print(B)