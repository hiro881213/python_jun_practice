# 5.1. 作成したパッケージをインポートする
# 5.1.5. ImportErrorが発生した場合の対処法
try:
    from lesson_package import utils
except:
    from lesson_package.tools import utils
