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

# test de plugin...
class Plugin(Abstract.Plugin):

    def name(self) -> str:
        return "FL Keys"



    def button(self, btn: int, shift: bool, press: bool) -> bool:
        if btn == Consts.BTN_PROJECT:
            pass # used for test for the moment

        elif btn == Consts.BTN_SELECT:
            print("tap fl keys!!!")

        else:
            return False

        return True
