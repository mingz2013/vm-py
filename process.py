# -*- coding: utf-8 -*-
"""
@FileName: process
@Time: 2020/2/4 14:14
@Author: zhaojm

Module Description

"""

from thread import Thread


class Process(object):
    """
    Process
    """

    def __init__(self):
        self.thread_list = []

    def run(self):
        t = Thread()
        self.thread_list.append(t)
        t.run()
