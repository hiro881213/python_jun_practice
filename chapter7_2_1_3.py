# 7.2. ファイルの活用
# 7.2.1. テンプレートを使って文章を作る
# 7.2.1.2. テンプレートの活用方法
import string

with open('design/email_template.txt') as f:
    t = string.Template(f.read())
    contents = t.substitute(name = 'Mike', contents= 'How are you?')
    print(contents)