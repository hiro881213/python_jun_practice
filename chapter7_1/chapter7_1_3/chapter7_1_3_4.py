# 7.1. ファイルの基本的な操作
# 7.1.3. ファイルの内容を読み込む
# ファイルを１行ずつ読み込む2
with open('../test.txt', 'r') as f:
    while True:
        line = f.readline()
        print(line, end='')

        if not line: break