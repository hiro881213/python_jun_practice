# 4.2. 関数の応用
# 4.2.3. lambdaの利用
# 曜日のリスト
l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri', 'sat', 'Sun']

# 文字列に関数を適用する関数
def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

def sample_func2(word):
    return word.lower()

change_words(l, sample_func)
print('---------------------------')
change_words(l, sample_func2)
print('---------------------------')

