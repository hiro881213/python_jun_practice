# 7.3. 圧縮ファイルの利用
# 7.3.1. tarファイルの圧縮と展開
# 7.3.1.3. tarファイルを展開せずに中身を確認する
import tarfile

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    with tr.extractfile('test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())