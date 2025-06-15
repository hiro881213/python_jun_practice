# 7.2. ファイルの活用
# 7.2.1. テンプレートを使って文章を作る
# 7.2.1.1. テンプレートの使い方
import string

s = """\
Hi $name.
$contents
Have a good day
"""

t = string.Template(s)