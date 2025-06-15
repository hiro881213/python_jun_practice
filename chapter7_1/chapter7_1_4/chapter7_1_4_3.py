# 7.1. ファイルの基本的な操作
# 7.1.4. ファイル内の位置を移動する
# seek
with open('../test.txt', 'r') as f:
    f.seek(5)
    print(f.read(1))