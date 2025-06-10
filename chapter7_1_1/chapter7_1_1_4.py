# 7.1. ファイルの基本的な操作
# 7.1.1. ファイルを作成する
# 7.1.1.2. print関数でもファイルに書き込める
f = open('test.txt', 'w')
f.write('Test\n')
print('I am print', file = f)
f.close()