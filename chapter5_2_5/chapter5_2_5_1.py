# 5.2. Pythonのライブラリの使い方
# 5.2.5. スクリプトが読み込まれる時の注意点
#__name__の表示
print(__name__)

# configの読み込み
import config

print('lesson:', __name__)

# animalの読み込み
import talk.animal

print('lesson:', __name__)
