# 7.1. ファイルの基本的な操作
# 7.1.4. ファイル内の位置を移動する
# ファイルの現在の位置を確認する
with open('test.txt', 'r') as f:
    print(f.tell())
    print(f.read(1))
    print(f.tell())