# 5.1. 作成したパッケージをインポートする
# 5.1.2. importの使い方
# 5.1.2.1. パッケージを読むこむ
# モジュール読み込み
from chapter5_1.chapter5_1_2 import lesson_package

# インポートした関数の呼び出し
r = lesson_package.utils.say_twice('hello')
print(r)