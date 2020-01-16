import io

f = io.StringIO()
f.write('string io test')
f.seek(0)
print(f.read())

f = io.BytesIO()
f.write(b'bytes io test')
f.seek(0)
print(f.read())
