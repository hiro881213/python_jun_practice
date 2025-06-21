# 7.4. さらに高度なファイルに関する操作
# 7.4.1. 一時ファイルを活用する
# 7.4.1.1. 一時ファイルの作成
import tempfile

with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())