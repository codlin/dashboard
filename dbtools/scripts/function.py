#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ma xiaoquan
# @Contact: xiaoquan.ma@nokia-sbell.com
# @File: function.py
# @Time: 2018/9/6 17:24
# @Desc:
import sys
import logging
log = logging.getLogger()

def set_log_level(log_level):
    eligible_log_levels = ('ERROR', 'WARNING', 'INFO', 'DEBUG')
    if log_level in eligible_log_levels:
        logging.basicConfig(stream=sys.stdout,
                            format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')
        _logger = logging.getLogger()
        _logger.setLevel(log_level)
        return _logger
    else:
        raise ValueError("Invalid log level '%s', should be in %s" % (log_level, eligible_log_levels))