import logging
import logging.handlers
import queue
import multiprocessing


# 创建日志队列
log_queue = queue.Queue(-1)

# 创建QueueHandler对象
handler = logging.handlers.QueueHandler(log_queue)
logger = logging.getLogger()
logger.addHandler(handler)

# 创建QueueListener对象
listener = logging.handlers.QueueListener(log_queue, handler)

# 启动QueueListener对象
listener.start()


def worker_process():
    # 在工作进程中记录日志
    logger.warning('This is a warning message from worker process')


# 创建并启动工作进程
process = multiprocessing.Process(target=worker_process)
process.start()
process.join()

# 停止QueueListener对象
listener.stop()