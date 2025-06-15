# 7.1. ファイルの基本的な操作
# 7.1.3. ファイルの内容を読み込む
# ファイルをチャンクごとに読み込む
with open('../test.txt', 'r') as f:
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)

        if not line:
            break