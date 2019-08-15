"""
ロギング ハンドラ.
main処理以外のログ情報をファイルに出力する.
"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# ハンドラ取得
get_handler = logging.FileHandler('logfile/logger2.log')
logger.addHandler(get_handler)

logger.info('from logger_lesson2')
