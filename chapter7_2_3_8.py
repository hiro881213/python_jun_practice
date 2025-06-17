# 7.2. ファイルの活用
# 7.2.3. 様々なファイル操作
# 7.2.3.4. ファイルやディレクトリの列挙
import os

os.mkdir('test_dir')
os.mkdir('test_dir/test_dir2')

print(os.listdir('test_dir'))