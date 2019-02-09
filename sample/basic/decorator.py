"""
デコレータ: 既存関数の処理の前後に処理を付け加えることができる.
"""


def print_info(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@print_info
def add_num(a, b):
    return a + b


print(add_num(1, 2))
