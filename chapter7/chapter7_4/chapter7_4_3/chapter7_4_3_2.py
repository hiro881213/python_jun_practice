# 7.4. さらに高度なファイルに関する操作
# 7.4.3. 時間にまつわるライブラリとバックアップファイル
# 7.4.3.1. datetimeの使い方
import datetime

now = datetime.datetime.now()
print(now.strftime('%d/%m/%y-%H%M%S%f'))