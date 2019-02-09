"""
リスト内包表記: Listの作成が簡単に書ける.
"""

tuple = (1, 2, 3, 4, 5)
list = []

# リスト内包表記を使わない場合
for i in tuple:
    if i % 2 == 0:
        list.append(i)
print(list)

# リスト内包表記を使う場合
list = [i for i in tuple if i % 2 == 0]
print(list)

# 辞書内包表記も使える
key = ['mon', 'tue', 'wed']
value = ['cofee', 'milk', 'water']

map = {x: y for x, y in zip(key, value)}
print(map)
