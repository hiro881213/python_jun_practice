# 7.4. さらに高度なファイルに関する操作
# 7.4.2. Pythonでターミナルのコマンドを実行する
# 7.4.2.2. shell=Trueを使ったコマンドの実行
import subprocess

subprocess.run('ls -al | grep test', shell = True)