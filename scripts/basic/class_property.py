"""
プロパティ: インスタンス変数の値を外部から読み取ったり、更新したりできないようにする.
ゲッター、セッター: 変数と関数名を一致させるのがポイント.
"""


class Person(object):
    """非公開のインスタンスを設定."""
    def __init__(self, name):
        self.__name = name  # 非公開のインスタンス変数

    def who(self):
        print(self.__name + 'です。')


person = Person('宇佐美')
person.who()  # インスタンスメソッドを介して__nameの値を調べることはできる
# person.__name  # これはエラーになる


print()


class Goods(object):
    """プロパティのゲッター、セッターを指定する."""
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # name プロパティ（ゲッター）
    @property
    def name(self):
        return self.__name

    # name プロパティ（セッター）
    @name.setter
    def name(self, value):
        self.__name = value

    # price プロパティ（ゲッター）
    @property
    def price(self):
        price = self.__price
        return f'{price}円'


goods = Goods('ball', 3000)
print(goods.name)
goods.name = 'glove'
print(goods.name)

print(goods.price)
# goods.price = 2000  # これはエラーになる
