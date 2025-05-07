# 2.1. 複数データを並列にまとめる
# 2.1.2. リストのデータを操作する
# 2.1.2.2. メソッドによるリストによる挿入/削除
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# appendメソッド
n.append(100)
print(n)

# insertメソッド
n.insert(0, 200)
print(n)

# popメソッド
n.pop()
print(n)

# インデックスでpopの取り出し先を指定する
n.pop(0)
print(n)

# del文1
del n[0]
print(n)

# del文2
del n
print(n)