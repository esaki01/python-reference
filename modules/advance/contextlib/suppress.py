import contextlib
import os

# try:
#     os.remove('aaa')
# except FileNotFoundError:
#     pass


with contextlib.suppress(FileNotFoundError):
    os.remove('aaa')
