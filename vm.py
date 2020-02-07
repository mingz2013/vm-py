# -*- coding: utf-8 -*-
"""
@FileName: vm
@Time: 2020/2/4 14:13
@Author: zhaojm

Module Description

"""

from binary_code.binary_file import BinaryFile
from call_frame import CallFrame
from instructions.instruction import new_instruction
from call_stack import Stack


class VM(object):
    """
    VM
    Virtual Machine
    """

    def __init__(self, filename):
        self.binary_file = BinaryFile(filename)  # 二进制文件解析后的数据
        self.stack = Stack()  # callstack
        self.call(self.binary_file.main_func)

    @property
    def cur_call_frame(self):
        return self.stack.top_node

    @property
    def pc(self):
        return self.stack.top_node.pc

    def add_pc(self, n):
        self.cur_call_frame.add_pc(n)

    def init(self):
        pass

    def run(self):
        while True:
            i = self.cur_call_frame.fetch()
            i_obj = new_instruction(i)
            i_obj.execute(self)

    def call(self, proto):
        """

        """
        cur_f = self.cur_call_frame
        f = CallFrame(proto)

        self.stack.push(f)

    def return_(self):
        """

        """
        f = self.stack.pop()
