# -*- coding: utf-8 -*-
"""
@FileName: vm
@Time: 2020/2/4 14:13
@Author: zhaojm

Module Description

"""

from process import Process


class VM(object):
    """
    VM
    Virtual Machine
    """

    def __init__(self):
        self.process_list = []

    def init(self):
        p = Process()
        self.process_list.append(p)
        p.init()

    def run(self):
        pass
