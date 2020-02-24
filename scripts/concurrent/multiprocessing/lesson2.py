"""
並列処理（マルチプロセス）プロセス数の指定、非同期.
"""

import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker1(i):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    return i


if __name__ == '__main__':
    with multiprocessing.Pool(3) as p:
        logging.debug(p.apply(worker1, (200,)))  # ブロック
        logging.debug('executed apply')
        p1 = p.apply_async(worker1, (100,))  # 非同期
        p2 = p.apply_async(worker1, (100,))  # 非同期
        logging.debug('executed')
        logging.debug(p1.get(timeout=6))
        logging.debug(p2.get())
