# 2.1. 複数データを並列にまとめる
# 2.1.3. リストのさまざまなメソッド
# 2.1.3.2. リストのソート
# sortメソッド(昇順)
r = [1, 2, 3, 4, 5, 1, 2, 3]
r.sort()
print(r)

# sortメソッド(降順)
r.sort(reverse=True)
print(r)

# reverseメソッド
r.sort()
r.reverse()
print(r)