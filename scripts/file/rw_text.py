"""
テキストファイルを読み書きする.
"""


text = """\
AAA
BBB
CCC
DDD
"""

# テキストファイルの書き込み
with open('test.txt', 'w') as f:
    f.write(text)

# テキストファイルの読み込み（テキスト全文をそのまま出力する）
with open('test.txt', 'r') as f:
    print(f.read())

print('################################\n')

# テキストファイルの読み込み（テキストを1行ずつ読み込んで出力する）
with open('test.txt', 'r') as f:
    while True:
        line = f.readline()
        print(line, end='')
        if not line:
            break

print('################################\n')

# テキストファイルの読み込み（チャンクごとに読み込んで出力する）
with open('test.txt', 'r') as f:
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break

print('################################\n')

# テキストファイルの読み込み（任意の箇所を飛ばして出力する）
with open('test.txt', 'r') as f:
    # 現在いる位置
    print(f.tell())
    print(f.read(1))
    f.seek(10)
    print(f.read(1))

print('################################\n')

# テキストファイルの読み書きを両方する
with open('test.txt', 'w+') as f:
    f.write(text)
    # 書き込んだのでシークを最初に戻す
    f.seek(0)
    print(f.read())
