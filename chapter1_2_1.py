# 1.2. 文字列のさまざまな操作方法
# 1.2.1. 文字列の基本的な使い方
# 1.2.1.1. 文字列を表示する
# 文字列を表示する
s = 'hello'
print(s)

# シングルクォートの中にシングルクォート
print('I don\'t know')

# シングルクォートの中にダブルクォート
print('say "I don\'t know"')

# ダブルクォートの中にダブルクォート
print("say \"I don't know\"")

# 文字列の途中に改行を入れる
print('hello. \nHow are you?')

# rawデータを出力
print(r'C:\name\name')

# 複数行にわたる文字列の出力
print("""
line1
line2
line3
""")

# 両端に改行を出さない
print("################")
print("""\
line1
line2
line3\
""")
print("################")

# 1.2.1.2. 文字列を連結する
# 文字列を繰り返し出力する
print('Hi. ' * 3)

# 文字列を連結する
print('Hi. ' * 3 + 'Mike. ')

# リテラル同士を連結する
print('Py' + 'thon')
print('Py''thon')

# 変数とリテラルを連結する
prefix = 'Py'
print(prefix + 'thon')

# 複数行にわたる文字列の連結
print('aaaaaaaaaaaaaaaaaaaaa'
      'bbbbbbbbbbbbbbbbbbbbb')

# 複数行にわたる文字列の連結2
s = 'aaaaaaaaaaaaaaaaaaaaa'\
      'bbbbbbbbbbbbbbbbbbbbb'

print(s)
