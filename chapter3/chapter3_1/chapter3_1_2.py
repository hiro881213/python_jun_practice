# 3.1. コードを読みやすくする
# 3.1.2. 長すぎる行を分割する
# \で分割する
s = 'aaaaaaaaaaa' \
     + 'bbbbbbbbbbbbb'

print(s)

# ()で分割する
s = ('aaaaaaaaa'
      + 'bbbbbbbbbb')

print(s)
