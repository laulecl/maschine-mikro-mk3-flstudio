"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	0.1 alpha

    Copyright (c) 2023 Laurent LECLUSE
]]
"""

import Context
import Consts
import patterns



class Context(Context.Abstract):

    def enabled(self) -> bool:
        return True



    def jog(self, jog: int, mode: int, press: bool, step: int) -> bool:
        if False:
            pass

        else:
            return False

        return True



    def button(self, btn: int, shift: bool, press: bool) -> bool:
        if False:
            pass

        else:
            return False

        return True


    def select(self, step: int, slow: bool):
        patterns.jumpToPattern(patterns.patternNumber() + step)

    def add(self): # todo à tester
        patterns.findFirstNextEmptyPat(1)