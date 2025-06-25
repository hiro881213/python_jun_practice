# 7.3. 圧縮ファイルの利用
# 7.3.2. Zipファイルの圧縮と展開
# 7.3.2.2. zipファイルを展開する
import zipfile

with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('zzz2')