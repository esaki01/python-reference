import contextlib


@contextlib.contextmanager
def tag(name):
    print('<{}>'.format(name))
    yield
    print('</{}>'.format(name))


with tag('h2'):
    print('test')
