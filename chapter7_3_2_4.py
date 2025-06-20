# 7.3. 圧縮ファイルの利用
# 7.3.2. Zipファイルの圧縮と展開
# 7.3.2.3. Zipファイルを展開せずに中身を確認する
import zipfile

with zipfile.ZipFile('test.zip', 'r') as z:
    with z.open('test_dir/test.txt') as f:
        print(f.read())