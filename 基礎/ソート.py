"""
sort(): リストの値をソートする.
sorted(): リストの値をコピーしてソートする.
"""

# 文字列の長さでソートする
words = ['chest', 'wind', 'holiday', 'knight', 'silence', 'hot']
words.sort(key=len)
print(words)

# 大文字小文字を区別せずにソートする
words = ['peach', 'ver3', 'Python', 'Pokemon', 'ver2']
new_words = sorted(words, key=str.lower)
print(new_words)


# 比較関数を自分で定義する
def size(item):
    size_list = ['XS', 'S', 'M', 'L']
    pos = size_list.index(item)
    return pos


# 比較関数でソートする
data = ['S', 'M', 'XS', 'L', 'M', 'M', 'XS', 'S', 'M', 'L', 'M']
data.sort(key=size)
print(data)

# ソート関数をラムダ式で書く
size_list = ['XS', 'S', 'M', 'L']
data = ['S', 'M', 'XS', 'L', 'M', 'M', 'XS', 'S', 'M', 'L', 'M']
data.sort(key=lambda item: size_list.index(item))
print(data)
