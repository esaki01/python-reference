"""
テキストファイルに追記する.
"""


import sys
from datetime import datetime

file = 'log.txt'

if len(sys.argv) < 2:
    sys.exit()

now = str(datetime.now())
memo = sys.argv[1]
line = '-'*10

with open(file, 'a') as f:
    f.write(now + '\n')
    f.write(memo + '\n')
    f.write(line + '\n')
