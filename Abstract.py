"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	1.0

    Copyright (c) 2022 Laurent LECLUSE
]]
"""

import ui
import midi
import plugins



class Context:

    def __init__(self, router):
        self.router = router



    def enabled(self) -> bool:
        return False



    def jog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        return False



    def button(self, btn: int, shift: bool, press: bool) -> bool:
        return False



    def pad(self, group: int, pad: int, shift: bool, pressure: int) -> bool:
        return False



    def padChangePressure(self, group: int, pad: int, pressure: int) -> bool:
        return False



class Plugin(Context):

    def __init__(self, router):
        super().__init__(router)



    def name(self) -> str:
        return "Name unknown"



    def enabled(self) -> bool:
        return ui.getFocusedPluginName() == self.name()
