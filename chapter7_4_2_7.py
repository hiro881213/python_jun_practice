# 7.4. さらに高度なファイルに関する操作
# 7.4.2. Pythonでターミナルのコマンドを実行する
# 7.4.2.3. popenの利用
import subprocess

p1 = subprocess.Popen(['ls', '-al'], stdout = subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'test'], stdin = p1.stdout, stdout = subprocess.PIPE)
p1.stdout.close()

output = p2.communicate()[0]
print(output)