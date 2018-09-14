#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import logging.handlers


def create_logger(name, level):
    log_levels = ('ERROR', 'WARNING', 'INFO', 'DEBUG')
    if level not in log_levels:
        raise ValueError("Invalid log level {}, should be in {}".format(
            level, log_levels))

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # create formatter
    formatter = logging.Formatter(
        "%(asctime)s %(filename)s:%(lineno)d [%(levelname)s]: %(message)s", '%Y-%m-%d %H:%M:%S')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def set_log_level(name, level):
    log_levels = ('ERROR', 'WARNING', 'INFO', 'DEBUG')
    if level not in log_levels:
        raise ValueError("Invalid log level {}, should be in {}".format(
            level, log_levels))

    logger = logging.getLogger(name)
    logger.setLevel(level)


logger = create_logger("DBTools", 'INFO')

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(1)

    logger.set_log_level("DBTools", sys.argv[0])
