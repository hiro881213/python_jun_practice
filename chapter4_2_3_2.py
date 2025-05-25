# 4.2. 関数の応用
# 4.2.3. lambdaの利用
# 曜日のリスト
l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri', 'sat', 'Sun']

# 文字列に関数を適用する関数
def change_words(words, func):
    for word in words:
        print(func(word))

# ラムダ関数を関数にして実行する
sample_func = lambda word: word.capitalize()
change_words(l, sample_func)

print('################')

# ラムダ関数を直接change_wordsの引数に入れる
change_words(l, lambda word: word.capitalize())