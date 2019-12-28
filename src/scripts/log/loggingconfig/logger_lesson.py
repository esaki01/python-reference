import logging.config

logging.config.dictConfig({
    'version': 1,

    # フォーマットの設定
    'formatters': {
        'sampleFormatter': {
            'format': '%(asctime)s %(message)s'
        }
    },
    # ハンドラの設定
    'handlers': {
        'sampleHandler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logfile/logger.log',
            'formatter': 'sampleFormatter',
            'level': logging.DEBUG
        }
    },
    # ロガーの対象一覧
    'root': {
        'handlers': ['sampleHandler'],
        'level': logging.WARNING,
    },
    'loggers': {
        'outputLogging': {
            'handlers': ['sampleHandler'],
            'level': logging.DEBUG,
            'propagate': 0
        }
    }
})

# 設定したロギングを使う
logger = logging.getLogger('outputLogging')

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

# rootのロギングを使う
logger = logging.getLogger(__name__)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
