# 4.1. 関数
# 4.1.2.　位置引数、キーワード引数、デフォルト引数
# 4.1.2.3. デフォルト引数
def menu(entree = 'beef', drink = 'wine', dessert = 'ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu()

# デフォルト引数を上書きする
print('############')
menu('chicken', drink = 'beer')