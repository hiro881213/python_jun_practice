# 7.4. さらに高度なファイルに関する操作
# 7.4.3. 時間にまつわるライブラリとバックアップファイル
# 7.4.3.4. バックアップファイルの作成
import os
import shutil
import datetime

now =  datetime.datetime.now()

file_name = 'test.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(file_name, now.strftime('%Y_%m_%d_%H_%M_%S')))

with open(file_name, 'w') as f:
    f.write('test')