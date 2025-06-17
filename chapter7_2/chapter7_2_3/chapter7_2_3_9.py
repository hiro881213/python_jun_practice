# 7.2. ファイルの活用
# 7.2.3. 様々なファイル操作
# 7.2.3.4. ファイルやディレクトリの列挙
import pathlib
import glob

pathlib.Path('test_dir/test_dir2/empty.txt').touch()
print(glob.glob('test_dir/test_dir2/*'))