"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	0.1 alpha

    Copyright (c) 2023 Laurent LECLUSE
]]
"""

import Consts
import Test
from Router import Router
import device
import time



class MaschineMikroMK3:

    def __init__(self):
        self.router = Router(self)
        self.shift = False
        self._pads = [False] * 17
        self._padShifts = [False] * 17
        self._buttons = [False] * 128
        self._btnShifts = [False] * 128
        self.initButtons()



    def initButtons(self):
        for btn in Consts.DEFAULTS:
            self.setBtnPressed(btn, True)

        time.sleep(0.2)

        for btn in Consts.DEFAULTS:
            self.setBtnPressed(btn, False)

        for btn in Consts.DEFAULTS:
            self.setBtnPressed(btn, Consts.DEFAULTS[btn]["pressed"])



    def onGlobalChange(self):
        pass



    def onControlChange(self, event):
        if event.controlNum == 2:  # Strip bypassed for use with assignments
            pass

        elif event.controlNum == 7:  # Jogs
            event.handled = True
            if event.controlVal == 1:
                step = 1
            else:
                step = -1
            self.router.jog(event.controlNum, self.shift, self.isBtnPressed(Consts.BTN_JOG), step)

        elif event.controlNum == Consts.BTN_RESTART:  # BTN Restart used as SHIFT KEY
            event.handled = True
            self.shift = event.controlVal > 0

        else:  # All other buttons
            event.handled = True
            if event.controlVal > 0:
                self._buttons[event.controlNum] = True
                self._btnShifts[event.controlNum] = self.shift
                self.router.button(event.controlNum, self._btnShifts[event.controlNum], True)
            else:
                self._buttons[event.controlNum] = False
                self.router.button(event.controlNum, self._btnShifts[event.controlNum], False)
                self._btnShifts[event.controlNum] = False



    def onPadPressure(self, event):
        event.handled = True
        pad = self._getPad(event)
        if event.pressure > 0 and not self._pads[pad]:
            self._pads[pad] = True
            self._padShifts[pad] = self.shift
            self.router.pad(self._getGroup(event), pad, self._padShifts[pad], event.pressure)

        elif event.pressure == 0 and self._pads[pad]:
            self._pads[pad] = False
            self.router.pad(self._getGroup(event), pad, self._padShifts[pad], 0)
            self._padShifts[pad] = False

        elif event.pressure > 0 and self._pads[pad]:
            self.router.padChangePressure(self._getGroup(event), pad, event.pressure)



    def _getPad(self, event):
        return event.controlNum - ((event.midiChan % 8 + 1) * 12 - 1)



    def _getGroup(self, event):
        return 12 - event.midiChan + event.midiChan % 4 + 1 + event.midiChan % 4



    def setBtnPressed(self, btn: int, pressed: bool):
        if pressed:
            controlVal = 127
        else:
            controlVal = 0

        self._buttons[btn] = pressed
        self._btnShifts[btn] = False
        device.midiOutMsg(176, 0, btn, controlVal)



    def isBtnPressed(self, btn: int):
        return self._buttons[btn]



    def isPadPressed(self, pad: int):
        return self._pads[pad]



    def isBtnShifted(self, btn: int):
        return self._btnShifts[btn]



    def isPadShifted(self, pad: int):
        return self._padShifts[pad]
