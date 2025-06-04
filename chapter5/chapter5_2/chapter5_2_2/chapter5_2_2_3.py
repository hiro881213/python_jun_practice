# 5.2. Pythonのライブラリの使い方
# 5.2.2. Pythonの標準ライブラリ
# 5.2.2.1. defaultdictを使用する
s = "aerawjitrpqwkaerafpevpeavmovvavaf"

# collectionライブラリ
from collections import defaultdict
d = defaultdict(int)

for c in s:
    d[c] += 1

print(d)