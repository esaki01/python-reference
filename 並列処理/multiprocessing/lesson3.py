"""
並列処理（マルチプロセス）lesson2 を map で書き換え.
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
        # r = p.map(worker1, [100, 200])  # ブロック
        r = p.map_async(worker1, [100, 200])  # 非同期
        # r = p.imap(worker1, [100, 200])  # Iterator
        logging.debug('executed')
        # logging.debug(r)
        logging.debug(r.get(timeout=6))
        # logging.debug([i for i in r])
