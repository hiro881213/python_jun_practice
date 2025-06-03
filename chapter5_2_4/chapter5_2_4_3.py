# 5.2. Pythonのライブラリの使い方
# 5.2.4. ライブラリインポートの注意点
# 5.2.4.2. ライブラリの場所
import collections

import termcolor

import lesson_package

import config

print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)