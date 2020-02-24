"""
並行処理（マルチスレッド）キュー.
"""

import logging
import threading
import time
import queue

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(queue):
    logging.debug('start')
    queue.put(100)
    time.sleep(5)
    queue.put(200)
    logging.debug('end')


def worker2(queue):
    logging.debug('start')
    logging.debug(queue.get())
    logging.debug(queue.get())  # get できる値が put されるまで待機する
    logging.debug('end')


if __name__ == '__main__':
    queue = queue.Queue()
    t1 = threading.Thread(target=worker1, args=(queue,))
    t2 = threading.Thread(target=worker2, args=(queue,))
    t1.start()
    t2.start()
