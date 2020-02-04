# -*- coding: utf-8 -*-
"""
@FileName: thread
@Time: 2020/2/4 14:14
@Author: zhaojm

Module Description

"""

from stack import Stack


class Thread(object):
    """thread"""

    def __init__(self):
        self.stack = Stack()

    def run(self):
        """
        run
        """
