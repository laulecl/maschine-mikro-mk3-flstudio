"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	1.0

    Copyright (c) 2022 Laurent LECLUSE
]]
"""


class Abstract:

    def __init__(self, router):
        self.router = router

    def enabled(self) -> bool:
        return False

    def jog(self, jog: int, mode: int, press: bool, step: int) -> bool:
        #print("JOG jog=" + str(jog) + ", mode=" + str(mode) + ", press=" + str(press) + ", step=" + str(step))
        return False

    def button(self, btn: int, shift: bool, press: bool) -> bool:
        # print("button " + self.router.mmmk3.test.btnName(btn) + ", shift=" + str(shift) + ", press=" + str(press))
        return False

    def pad(self, group: int, pad: int, shift: bool, pressure: int) -> bool:
        return False

    def padChangePressure(self, group: int, pad: int, pressure: int) -> bool:
        return False


"""
Example :

import Context
import Consts

class Context(Context.Abstract):

    #def __init__(self, router):
    #    AbstractContext.__init__(self, router)

    def enabled(self) -> bool:
        return True

    def jog(self, jog: int, mode: int, press: bool, step: int) -> bool:
        if mode == Consts.JOG_VOLUME:
            self.volume(step, press)

        else:
            return False

        #print("CHANNEL JOG jog=",jog,", mode=",mode,", press=",press,", step=",str(step))
        return True


"""