# 1.2. 文字列のさまざまな操作方法
# 1.2.2. 文字列のインデックスとスライスを使う
# 1.2.2.1. 文字列のインデックス
word = 'python'

# 文字列のインデックス
print(word[0])
print(word[1])
print(word[-1])

# 1.2.2.2. 文字列のスライス
# 文字列のスライス
print(word[0:2])
print(word[2:5])
print(word[2:])

# 文字列の変更
word2 = 'python'
word2 = 'j' + word2[1:]

print(word2)