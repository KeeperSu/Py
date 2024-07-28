#!/usr/bin/python
# Summary: logging方法的一些使用
import logging
import sys
import multiprocessing
import time
from logging.handlers import RotatingFileHandler, QueueHandler, QueueListener

FMT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


class MyLogger:
    def __init__(self, name: str, output: str = None, fmt=FMT, level=logging.INFO):
        self.name = name
        self.fmt = fmt
        self.level = level
        self.output = output
        self.logger = self.build_logger()

    def build_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)
        if self.name not in {"root"}:
            self.init_steam_handler(logger)
        if self.output is not None:
            self.init_file_handler(self.output, logger)
        return logger

    def init_steam_handler(self, logger: logging.Logger, level=None):
        # create and set handler
        handler = logging.StreamHandler(stream=sys.stdout)
        handler.setFormatter(logging.Formatter(self.fmt))
        if level is None:
            level = self.level
        handler.setLevel(level)
        # add handler to logger
        logger.addHandler(handler)

    def init_file_handler(self, log_path: str, logger: logging.Logger, level=None):
        handler = RotatingFileHandler(log_path)
        handler.setFormatter(logging.Formatter(self.fmt))
        if level is None:
            level = self.level
        handler.setLevel(level)
        logger.addHandler(handler)

    def add_queue_handler(self, q):
        handler = QueueHandler(q)
        self.logger.addHandler(handler)


logger0 = MyLogger("root", output="output.log")


def gen_listener(q, logger: MyLogger):
    # formatter = logging.Formatter(FMT)
    # handler = logging.StreamHandler()
    # handler.setFormatter(formatter)
    return QueueListener(q, *logger0.logger.handlers)


logger2 = MyLogger("INFER_FRAMEWORK")


def task(task_id: int):
    # print(task_id)
    logger2.logger.info(f"TaskID-{task_id} is processing")


if __name__ == '__main__':
    multiprocessing.Pool()
    logger1 = MyLogger("MASK")
    logger1.logger.info("process main process start ")
    process_list = []
    que = multiprocessing.Queue(-1)
    logger2.add_queue_handler(que)
    for idx in range(3):
        one_process = multiprocessing.Process(target=task, args=(idx, ))
        one_process.start()
        process_list.append(one_process)

    listener = gen_listener(que, logger2)
    listener.start()
    for p in process_list:
        p.join()

    listener.stop()
    logger1.logger.info("process main process done ")
    logger1.logger.info("--------------------------")
