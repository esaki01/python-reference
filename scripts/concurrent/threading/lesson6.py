"""
並行処理（マルチスレッド）Lock.
"""

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

# Lock なし
# def worker1(d):
#     logging.debug('start')
#     i = d['counter']  # {'counter': 0}
#     time.sleep(5)
#     d['counter'] = i + 1  # {'counter': 1}
#     logging.debug(d)
#     logging.debug('end')
#
#
# def worker2(d):
#     logging.debug('start')
#     i = d['counter']  # {'counter': 0}
#     d['counter'] = i + 1  # {'counter': 1}
#     logging.debug(d)
#     logging.debug('end')
#
#
# if __name__ == '__main__':
#     d = {'counter': 0}
#     t1 = threading.Thread(target=worker1, args=(d, ))
#     t2 = threading.Thread(target=worker2, args=(d, ))
#     t1.start()
#     t2.start()


# Lock あり
def worker1(d, lock):
    logging.debug('start')
    with lock:
        i = d['counter']  # {'counter': 0}
        time.sleep(5)
        d['counter'] = i + 1  # {'counter': 1}
        logging.debug(d)
        # with lock:  # RLock を使うと外のlockがまだ解放されていなくてもlockできる
        #     d['counter'] = i + 1
    logging.debug('end')


def worker2(d, lock):
    logging.debug('start')
    with lock:  # lock.acquire(), lock.release() で囲んでもOK
        i = d['counter']  # {'counter': 0}
        d['counter'] = i + 1  # {'counter': 1}
        logging.debug(d)
    logging.debug('end')


if __name__ == '__main__':
    d = {'counter': 0}
    lock = threading.Lock()
    # lock = threading.RLock()
    t1 = threading.Thread(target=worker1, args=(d, lock))
    t2 = threading.Thread(target=worker2, args=(d, lock))
    t1.start()
    t2.start()
