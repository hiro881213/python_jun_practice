# 5.2. Pythonのライブラリの使い方
# 5.2.2. Pythonの標準ライブラリ
# 5.2.2.1. defaultdictを使用する
s = "aerawjitrpqwkaerafpevpeavmovvavaf"

d = {}

# 文字列に含まれるアルファベットを数える
for c in s:
    if c not in d:
        d[c] = 0

    d[c] += 1

print(d)
