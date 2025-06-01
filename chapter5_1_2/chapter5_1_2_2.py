# 5.1. 作成したパッケージをインポートする
# 5.1.2. importの使い方
# 5.1.2.1. パッケージを読むこむ
# 関数だけをインポートする
from lesson_package.utils import say_twice

r = say_twice('hello')
print(r)