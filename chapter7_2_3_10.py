# 7.2. ファイルの活用
# 7.2.3. 様々なファイル操作
# 7.2.3.5. 高度なファイル操作
import shutil
import glob

shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt')
print(glob.glob('test_dir/test_dir2/*'))