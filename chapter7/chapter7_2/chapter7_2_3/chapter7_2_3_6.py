# 7.2. ファイルの活用
# 7.2.3. 様々なファイル操作
# 7.2.3.3. シンボリックリンクやディレクトリ、ファイルの作成
# 中身が空のファイルを作成する
import pathlib

pathlib.Path('empty.txt').touch()