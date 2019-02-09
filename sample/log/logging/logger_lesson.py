"""
ロギング.
一番シンプルにログをファイルに出力する方法.
"""

import logging

# フォーマットを定義
formatter = '%(levelname)s : %(asctime)s : %(message)s'

# ロギングの基本設定(debugレベルを指定)
logging.basicConfig(filename='logfile/logger.log', level=logging.DEBUG, format=formatter)

# logging のみの書き方
logging.info('from main')
