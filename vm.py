# -*- coding: utf-8 -*-
"""
@FileName: vm
@Time: 2020/2/4 14:13
@Author: zhaojm

Module Description

"""

from binary_code.binary_file import BinaryFile
from call_stack.call_frame import CallFrame
from instructions.instruction import new_instruction
from call_stack.call_stack import CallStack


class VM(object):
    """
    VM
    Virtual Machine
    """

    def __init__(self, filename):
        self.binary_file = BinaryFile(filename)  # 二进制文件解析后的数据
        self.stack = CallStack()  # callstack

    def init(self, args):
        """
        vm call, 初始执行
        """
        results = []
        f = CallFrame(self.binary_file.main_func, args, results)
        self.stack.push(f)

        self.loop()

    def loop(self):
        while True:
            data = self.cur_call_frame.fetch()
            inst = new_instruction(data)
            inst.execute(self)

    @property
    def cur_call_frame(self):
        return self.stack.top_node

    @property
    def pc(self):
        return self.stack.top_node.pc

    def add_pc(self, n):
        self.cur_call_frame.add_pc(n)

    def call(self, nArgs, nResults):
        """

        对于调用者函数：

        函数调用的时候，
        1 先将结果寄存器按顺序推入栈
        2 再将参数寄存器推入栈
        3 再将调用的函数原型推入栈
        4 执行call指令

        执行函数调用，
        1 先弹出函数原型
        2 再弹出参数列表
        3 再弹出结果列表



        对于被调用者函数：

        函数调用的时候，
        1 帧里面，保存了参数列表，结果列表
        2 执行字节码，可修改结果列表
        3 调用结束，最后执行ret指令

        """
        cur_f = self.cur_call_frame

        proto = self.cur_call_frame.pop()
        args = []
        for i in range(nArgs):
            args.append(self.cur_call_frame.pop())
        results = []
        for i in range(nResults):
            results.append(None)

        f = CallFrame(proto, args, results)

        self.stack.push(f)

    def ret(self):
        """
        函数返回的时候，
        1 取出结果列表
        2 弹出栈帧
        3 将结果列表压入调用者的栈帧

        """
        f = self.stack.pop()

        results = f.results

        for i in results:
            self.cur_call_frame.push(i)
