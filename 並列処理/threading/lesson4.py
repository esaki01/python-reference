"""
並行処理（マルチスレッド）スレッドをループで生成.
"""

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


if __name__ == '__main__':
    # threads = []
    # for _ in range(5):
    #     t = threading.Thread(target=worker1)
    #     t.setDaemon(True)
    #     t.start()
    #     threads.append(t)
    # for thread in threads:
    #     thread.join()

    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.setDaemon(True)
        t.start()

    print(threading.enumerate())
    for thread in threading.enumerate():
        if thread is threading.currentThread():
            print(thread)
            continue
        thread.join()
