# 7.1. ファイルの基本的な操作
# 7.1.2. with文を使ってファイルを開く
with open('text.txt', 'w') as f:
    f.write('Test')