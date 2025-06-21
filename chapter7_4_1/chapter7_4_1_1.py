# 7.4. さらに高度なファイルに関する操作
# 7.4.1. 一時ファイルを活用する
# 7.4.1.1. 一時ファイルの作成
import tempfile

with tempfile.TemporaryFile(mode = 'w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())