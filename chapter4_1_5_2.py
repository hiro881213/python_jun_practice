# 4.1. 関数
# 4.1.5. キーワード引数を辞書化してまとめる
# キーワード引数を辞書にして渡す
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}

menu(**d)