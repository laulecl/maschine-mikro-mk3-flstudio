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



    def jog(self, jog: int, mode: int, press: bool, step: int) -> bool:
        # print("JOG jog=" + str(jog) + ", mode=" + str(mode) + ", press=" + str(press) + ", step=" + str(step))
        return False



    def button(self, btn: int, shift: bool, press: bool) -> bool:
        # print("button " + self.router.mmmk3.test.btnName(btn) + ", shift=" + str(shift) + ", press=" + str(press))
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
