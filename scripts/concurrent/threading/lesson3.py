"""
並行処理（マルチスレッド）デーモンスレッド.
"""

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


def worker2():
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')


if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    t1.setDaemon(True)  # worker1の処理を待たずにプログラムを終了する（worker1も強制終了する）
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print('started')
    t1.join()  # worker1を強制終了するのではなく、終わるまで待つ
    # t2.join()
