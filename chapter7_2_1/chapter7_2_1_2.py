# 7.2. ファイルの活用
# 7.2.1. テンプレートを使って文章を作る
# 7.2.1.2. テンプレートの活用方法
s = """\
Hi $name.
$contents
Have a good day.
"""

with open('design/email_template.txt', 'w') as f:
    f.write(s)