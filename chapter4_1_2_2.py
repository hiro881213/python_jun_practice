# 4.1. 関数
# 4.1.2.　位置引数、キーワード引数、デフォルト引数
# 4.1.2.2. キーワード引数
def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu(entree = 'beef', dessert = 'ice', drink = 'beer')

# キーワード引数と位置引数を混ぜて使う
menu('beef', dessert = 'ice', drink = 'beer')
