"""
無名関数（匿名関数、ラムダ式）: 関数を定義することなく処理ができる.
"""


def area(w, h):
    return w * h


# lambdaを使わない場合
num = area(3, 4)
print(num)

# lambdaを使う場合（一旦変数に入れる）
func = lambda w, h: w * h
num = func(3, 4)
print(num)

# lambdaを使う場合（変数に入れない）
num = (lambda w, h: w * h)(3, 4)
print(num)

# 引数の初期値、キーワード引数の利用
price = lambda burger=1, potato=0: burger * 240 + potato * 100
num = price(potato=2)
print(num)
