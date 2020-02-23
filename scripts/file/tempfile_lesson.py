import tempfile

# 一時ファイルの作成
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# 一時ディレクトリの作成
with tempfile.TemporaryDirectory() as td:
    print(td)

# ファイルの作成
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# ディレクトリの作成
temp_dir = tempfile.mkdtemp()
print(temp_dir)
