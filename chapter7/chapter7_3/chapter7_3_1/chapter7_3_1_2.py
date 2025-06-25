# 7.3. 圧縮ファイルの利用
# 7.3.1. tarファイルの圧縮と展開
# 7.3.1.2. 圧縮してtarファイルを作成する
import tarfile

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    tr.extractall('test_dir')