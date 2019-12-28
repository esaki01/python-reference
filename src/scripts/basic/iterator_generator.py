"""
イテレータ: 要素を反復して取り出すことのできるインタフェース.
ジェネレータ: イテレータの一種で、1要素を取り出す度に処理を行い要素をジェネレートする.
"""

# イテラブルからイテレータを作る
colors = ['red', 'blue', 'green', 'yellow']
colors_iter = iter(colors)
print(type(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
# print(next(colors_iter)) StopIteration Error
print()


# ジェネレータ関数からイテレータを作る
def menu_generator():
    yield 'ワイン'
    yield 'サラダ'
    yield 'スープ'
    yield 'ステーキ'
    yield 'アイスクリーム'


menu = menu_generator()
print(type(menu))
print(next(menu))
print(next(menu))
print(next(menu))
print(next(menu))
print(next(menu))
print()


# for-inでも書ける
menu = menu_generator()  # generatorをすべて取り出してしまっているのでもう一度生成
for item in menu:
    print(item)
print()

# ジェネレータ式からイテレータを作る
odd_gen = (odd for odd in range(1, 6, 2))  # ()でジェネレータ内包表記
print(next(odd_gen))
print(next(odd_gen))
print(next(odd_gen))
print()


# ジェネレータをリストに変換する
even_data = (even for even in range(0, 10, 2))
print(list(even_data))

