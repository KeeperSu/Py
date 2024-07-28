import multiprocessing
import logging
import os
from logging.handlers import QueueHandler, QueueListener


def func(arg):
    logging.info('Process/function with argument {} and PID {}'.format(arg, os.getpid()))


def Process_init(q):
    queue_handler = QueueHandler(q)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(queue_handler)


if __name__ == '__main__':
    print('Main Started')
    mp_queue = multiprocessing.Queue()
    lg_handler = logging.StreamHandler()

    lg_handler.setFormatter(logging.Formatter("%(levelname)s: %(asctime)s - %(process)s - %(message)s"))

    queue_listener = QueueListener(mp_queue, lg_handler)
    queue_listener.start()

    process_pool = multiprocessing.Pool(2, Process_init, [mp_queue])
    process_pool.map(func, [1, 2])
    process_pool.close()
    process_pool.join()

    queue_listener.stop()
    print('Main Ended')
