"""
クラスの継承.
"""


# スーパークラス
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print('やあ！')


# サブクラス
class Player(Person):
    def __init__(self, name, age, number, position):
        super().__init__(name, age)
        self.number = number
        self.position = position

    def hello(self, name=None):
        if name:
            print(f'{name}さん、こんにちは！')
        else:
            super().hello()


player = Player('青木', 16, 10, 'MF')
print(player.name, player.age, player.number, player.position)
player.hello('青木')
player.hello()

