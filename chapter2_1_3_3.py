# 2.1. 複数データを並列にまとめる
# 2.1.3. リストのさまざまなメソッド
# 2.1.3.3. 文字列の分割

s = 'My name is Mike.'

# splitメソッド
to_split = s.split(' ')
print(to_split)

# 区切り文字が存在しない場合
to_split2 = s.split('!!!!!')
print(to_split2)
