# 5.1. 作成したパッケージをインポートする
# 5.1.2. importの使い方
# 5.1.2.1. パッケージを読むこむ
# モジュール読み込み
import lesson_package.utils

# インポートした関数の呼び出し
r = lesson_package.utils.say_twice('hello')
print(r)