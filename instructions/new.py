# -*- coding: utf-8 -*-
"""
@FileName: new
@Time: 2020/2/4 15:44
@Author: zhaojm

Module Description

"""

from .nop import Nop


def new_instruction(opcode):
    opcode_map = {
        0x11: Nop,
    }
    return opcode_map.get(opcode)
