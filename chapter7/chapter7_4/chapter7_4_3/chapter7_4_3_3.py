# 7.4. さらに高度なファイルに関する操作
# 7.4.3. 時間にまつわるライブラリとバックアップファイル
# 7.4.3.1. datetimeの使い方
import datetime

today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))