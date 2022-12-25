"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	0.1 alpha

    Copyright (c) 2023 Laurent LECLUSE
]]
"""

import Abstract
import Consts
import patterns
import transport
import ui
import midi



class Context(Abstract.Context):

    def enabled(self) -> bool:
        return ui.getFocusedFormID() == midi.widPlaylist



    def jog(self, jog: int, mode: int, press: bool, step: int) -> bool:
        if mode == Consts.JOG_DEFAULT:
            transport.globalTransport(midi.FPT_PatternJog, step)

        else:
            return False

        return True



    def button(self, btn: int, shift: bool, press: bool) -> bool:
        if False:
            pass

        else:
            return False

        return True


    def add(self): # todo à tester
        patterns.findFirstNextEmptyPat(1)