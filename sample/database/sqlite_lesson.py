import sqlite3

conn = sqlite3.connect('sqlite_lesson.db')
# conn = sqlite3.connect(':memory:')  # インメモリの場合

# これに対して操作する
curs = conn.cursor()

# テーブルの作成
curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
)
conn.commit()

# インサートする
curs.execute(
    'INSERT INTO persons(name) values("Mike")'
)
conn.commit()

# アップデートする
curs.execute(
    'UPDATE persons set name = "Michel" WHERE name = "Mike"'
)
conn.commit()

# デリートする
curs.execute(
    'DELETE FROM persons WHERE name = "Michel"'
)
conn.commit()

# セレクトする
curs.execute('SELECT * FROM persons')
print(curs.fetchall())
curs.close()

conn.close()
