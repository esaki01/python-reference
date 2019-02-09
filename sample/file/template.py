"""
テンプレート: 読み込み専用のファイルを扱いたいときに使用する.
"""


import string

# 読み込み専用ファイルを開く
with open('template.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='How are you?')
print(contents)
