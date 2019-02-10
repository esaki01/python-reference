"""
doctest: メソッド例を書きたいときに主に使う.
"""


class Cal(object):

    @staticmethod
    def add_num_and_double(x, y):
        """引数同士を足して2倍する.

        >>> c = Cal()
        >>> c.add_num_and_double(1, 1)
        4

        >>> c.add_num_and_double('1', '1')
        Traceback (most recent call last):
        ...
        ValueError
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
