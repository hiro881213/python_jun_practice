# 7.4. さらに高度なファイルに関する操作
# 7.4.3. 時間にまつわるライブラリとバックアップファイル
# 7.4.3.1. datetimeの使い方
import datetime

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H%M%S%f'))