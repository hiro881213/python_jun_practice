# 5.2. Pythonのライブラリの使い方
# 5.2.5. スクリプトが読み込まれる時の注意点
# main関数を使った書き方
from talk import animal2

def main():
    print(animal2.sing())

if __name__ == '__main__':
    main()