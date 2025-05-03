# 1.2. 文字列のさまざまな操作方法
# 1.2.1. 文字列の基本的な使い方
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