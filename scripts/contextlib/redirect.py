import contextlib
import logging
import sys

with open('log/stdout.log', 'w') as f:
    with contextlib.redirect_stdout(f):
        help(sys.stdout)

with open('log/stderr.log', 'w') as f:
    with contextlib.redirect_stderr(f):
        logging.error('Error!')
