# 7.4. さらに高度なファイルに関する操作
# 7.4.3. 時間にまつわるライブラリとバックアップファイル
# 7.4.3.2. 日付・時刻の計算
import datetime

now = datetime.datetime.now()
print(now)

d = datetime.timedelta(weeks = -1)
print(now + d)