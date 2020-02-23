import functools


def d(f):
    @functools.wraps(f)
    def w():
        """Wrapper docstring"""
        print('decorator')
        return f()

    return w


@d
def example():
    """Example docstring"""
    print('example')


print(example.__doc__)
help(example)
