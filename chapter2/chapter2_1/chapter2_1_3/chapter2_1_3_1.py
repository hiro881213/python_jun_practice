# 2.1. 複数データを並列にまとめる
# 2.1.3. リストのさまざまなメソッド
# 2.1.3.1. 基本的なリストのメソッド

r = [1, 2, 3, 4, 5, 1, 2, 3]

# indexメソッド
print(r.index(3))

# indexメソッド2
print(r.index(3, 3))

# countメソッド
print(r.count(3))

# in演算子とif文
if 5 in r:
    print('exist')