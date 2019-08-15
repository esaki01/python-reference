"""
クラスメソッド: オブジェクトを生成しないで関数を使用できる.
スタティックメソッド: オブジェクトを生成しないで関数を使用できる.

ただし、クラス変数へのアクセス方法が違う.詳しくはnotebookで.
"""


class Person(object):

    # クラス変数
    kind = 'human'

    def __init__(self):
        # インスタンス変数
        self.x = 100

    # オブジェクトを生成しないで関数を使いたいとき
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    # class objectの外に定義してもいいが、Personに関する関数だということがわかりにくくなる
    @staticmethod
    def about(year):
        print('about human {}'.format(year))


print(Person.kind)
print(Person.what_is_your_kind())
Person.about(1999)
