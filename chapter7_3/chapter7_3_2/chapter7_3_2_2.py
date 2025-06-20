# 7.3. 圧縮ファイルの利用
# 7.3.2. Zipファイルの圧縮と展開
# 7.3.2.1. 圧縮してzipファイルを作成する
# zipファイルの作成２
import zipfile
import glob

with zipfile.ZipFile('test.zip', 'w') as z:
    for f in glob.glob('test_dir/**', recursive= True):
        print(f)
        z.write(f)