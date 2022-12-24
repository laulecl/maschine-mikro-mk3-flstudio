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
import channels
import ui
import midi
import plugins



class Context(Context.Abstract):

    def enabled(self) -> bool:
        return ui.getFocusedFormID() == midi.widPlugin and plugins.isValid(channels.selectedChannel())



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



    def pad(self, group: int, pad: int, shift: bool, pressure: int):
        if False
            pass

        return True
