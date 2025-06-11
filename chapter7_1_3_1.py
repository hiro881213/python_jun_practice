# 7.1. ファイルの基本的な操作
# 7.1.3. ファイルの内容を読み込む
# ファイルを用意する
s = """\
AAA
BBB
CCC
DDD
"""

with open('test.txt', 'w') as f:
    f.write(s)