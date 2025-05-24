# 4.1. 関数
# 4.1.5. キーワード引数を辞書化してまとめる
# キーワード引数
def menu(entree = 'beef', drink = 'wine'):
    print(entree, drink)

menu(entree = 'beef', drink = 'coffee')

# キーワード引数を辞書型で受け取る
def menu2(**kwargs):
    print(kwargs)

menu2(entree = 'beef', drink = 'coffee')