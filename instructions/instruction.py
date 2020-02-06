# -*- coding: utf-8 -*-
"""
@FileName: instruction
@Time: 2020/2/4 15:37
@Author: zhaojm

Module Description

"""


class Instruction(object):
    """

    """

    def fetch_operands(self):
        """
        从字节码中提取操作数
        """

    def execute(self, frame):
        """
        执行
        """


class Nop(Instruction):
    """
    Nop，
    """
    pass


def new_instruction(opcode):
    """
    factory
    """
    opcode_map = {
        0x11: Nop,
    }
    return opcode_map.get(opcode)
