# 7.2. ファイルの活用
# 7.2.3. 様々なファイル操作
# 7.2.3.3. シンボリックリンクやディレクトリ、ファイルの作成
import os

# シンボリックリンク
os.symlink('rename.txt', 'symlink.txt')

# ディレクトリを作成
os.mkdir('test_dir')