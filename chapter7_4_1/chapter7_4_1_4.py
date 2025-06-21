# 7.4. さらに高度なファイルに関する操作
# 7.4.1. 一時ファイルを活用する
# 7.4.1.2. 一時ディレクトリの作成
import tempfile

with tempfile.TemporaryDirectory() as td:
    print(td)

temp_dir = tempfile.mkstemp()
print(temp_dir)