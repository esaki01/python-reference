"""
フォルダがなければ作成し、ファイルがあれば上書きするか確認する.
"""

import os
from random import randint

# 保存フォルダとファイルパス
folder = './data/'
file = folder + 'sample.txt'


def filewrite():
    """ファイルを保存する."""
    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(file, 'w', encoding='uft_8') as f:
        num = randint(0, 100)
        f.write(f'{num}が出ました。')
        print('ファイルを保存しました。')


# 既存のファイルの有無チェック
if os.path.exists(file):
    while True:
        answer = input('上書きしていいですか？（y / n）')
        if answer == 'y':
            filewrite()
            break
        elif answer == 'n':
            break
else:
    filewrite()
