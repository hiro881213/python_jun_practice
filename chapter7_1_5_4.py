# 7.1. ファイルの基本的な操作
# 7.1.5. 書き込みと読み込みを同時に行いたいとき
s = """\
AAA
BBB
CCC
DDD
"""

with open('test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)