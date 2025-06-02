# 5.2. Pythonのライブラリの使い方
# 5.2.1. すぐに使える便利な組み込み関数
# 5.2.1.2. sorted関数で並び替える
ranking = {
    'A': 100,
    'B': 85,
    'C': 92
}

# sorted関数を使わない
for key in ranking:
    print(key)

# キーの順番で並べる
print(sorted(ranking))

# バリューの値で並べる
print(sorted(ranking, key = ranking.get))