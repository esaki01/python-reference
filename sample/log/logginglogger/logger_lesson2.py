"""
logger_lesson.pyで呼び出す用.
"""

import logging

logger = logging.getLogger(__name__)
# このファイルだけのログレベルに変更できる
logger.setLevel(logging.DEBUG)


def do_something():
    logger.info('from logger_lesson2')
