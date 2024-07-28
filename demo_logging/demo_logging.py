#!/usr/bin/python
# Summary: logging方法的一些使用
import logging
import sys
import time
from logging.handlers import RotatingFileHandler


class MyLogger:
    def __init__(self, name: str, output: str = None,
                 fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                 level=logging.INFO):
        self.name = name
        self.fmt = fmt
        self.level = level
        self.output = output
        self.logger = self.build_logger()

    def build_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)
        if self.name != "root":
            self.add_steam_handler(logger)
        if self.output is not None:
            self.add_file_handler(self.output, logger)
        return logger

    def add_steam_handler(self, logger: logging.Logger, level=None):
        # create and set handler
        handler = logging.StreamHandler(stream=sys.stdout)
        handler.setFormatter(logging.Formatter(self.fmt))
        if level is None:
            level = self.level
        handler.setLevel(level)
        # add handler to logger
        logger.addHandler(handler)

    def add_file_handler(self, log_path: str, logger: logging.Logger, level=None):
        handler = RotatingFileHandler(log_path)
        handler.setFormatter(logging.Formatter(self.fmt))
        if level is None:
            level = self.level
        handler.setLevel(level)
        logger.addHandler(handler)


if __name__ == '__main__':
    logger0 = MyLogger("root", output="output.log")
    logger1 = MyLogger("MASK")
    logger2 = MyLogger("INFER_FRAMEWORK")
    logger1.logger.info("logger1 add info 1")
    logger2.logger.info("logger2 add info 1")
    logger1.logger.info("logger1 add info 2")
