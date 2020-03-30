"""
ロギング ロガー.
基本設定を引き継いで、特定の処理にだけログの設定を変更することができる仕組み.
"""
import logging

from ログ.logginglogger import logger_lesson2

# フォーマットを定義
formatter = '%(levelname)s : %(asctime)s : %(message)s'

# ロギングの基本設定(infoレベルを指定)
logging.basicConfig(filename='logfile/logger.log', level=logging.DEBUG, format=formatter)
logging.info('from main info')

# 現在のロギングの情報を取得(引数はファイル名)
logger = logging.getLogger(__name__)
# ロギングの設定を DEBUG に変更
logger.setLevel(logging.DEBUG)
logger.debug('from main debug')

# 別ファイルから呼び出す
logger_lesson2.do_something()
