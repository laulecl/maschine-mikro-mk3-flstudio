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
import transport
import midi



class Context(Abstract.Context):

    def enabled(self) -> bool:
        return True



    def jog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        #if mode == Consts.JOG_DEFAULT:
        #    transport.globalTransport(midi.FPT_Jog, step)

        #elif mode == Consts.JOG_SHIFT:
        #    transport.globalTransport(midi.FPT_Jog2, step)
        if False:
            pass
        else:
            return False

        return True



    def button(self, btn: int, shift: bool, press: bool) -> bool:
        if btn == Consts.BTN_PROJECT:
            pass  # used for test for the moment

        elif btn == Consts.BTN_BROWSER:  # change current window
            transport.globalTransport(midi.FPT_NextWindow, 1)

        else:
            return False

        return True



    def browser(self):
        transport.globalTransport(midi.FPT_F8, 1)
