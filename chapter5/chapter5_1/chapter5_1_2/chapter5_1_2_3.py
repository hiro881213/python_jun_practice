# 5.1. 作成したパッケージをインポートする
# 5.1.2. importの使い方
# 5.1.2.3. asを使って違う名前で読み込む
from lesson_package import utils as u

r = u.say_twice('hello')
print(r)