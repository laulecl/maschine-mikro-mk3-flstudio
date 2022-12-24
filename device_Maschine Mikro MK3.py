# name=Native Instruments Maschine Mikro MK3
# supportedHardwareIds=00 20 6B 02 00 04 04 ## Changer
# url=

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



class MaschineMikroMK3:

    def __init__(self):
        self.router = Router(self)

        self.shift = False
        self._pads = {}
        self._padShifts = {}
        self._buttons = {}
        self._btnShifts = {}

        for i in range(17):
            self._pads[i] = False
            self._padShifts[i] = False

        for i in range(128):
            self._buttons[i] = False
            self._btnShifts[i] = False

        self.initButtons()



    def initButtons(self):
        for btn in Consts.DEFAULTS:
            self.setBtnPressed(btn, Consts.DEFAULTS[btn]["pressed"])



    def onControlChange(self, event):
        if event.controlNum == 2:  # Strip bypassed for use with assignments
            return None
            # Test.printEvent(event, "")
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



    def onMidiIn(self, event):
        if event.status == 147:  # No catch Note HITS, Just Press via OnKeyPressure
            event.handled = True



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



# ----------------------------------------------------------------------------------------


def OnKeyPressure(event):
    global _mmmk3
    _mmmk3.onPadPressure(event)
    # Test.printEvent(event, "OnKeyPressure")



def OnControlChange(event):
    global _mmmk3
    _mmmk3.onControlChange(event)
    # Test.printEvent(event, "onControlChange")



def OnMidiIn(event):
    global _mmmk3
    _mmmk3.onMidiIn(event)
    # Test.printEvent(event,"OnMidiIn")



# def OnMidiMsg(event):
#     Test.printEvent(event, "OnMidiMsg")


def OnProgramChange(event):
    Test.printEvent(event, "OnProgramChange")



def OnPitchBend(event):
    Test.printEvent(event, "OnPitchBend")



def OnChannelPressure(event):
    Test.printEvent(event, "OnChannelPressure")



def OnSysEx(event):
    Test.printEvent(event, "OnSysEx")



def OnInit():
    global _mmmk3
    print('Loaded MIDI script for Native Instruments Maschine Mikro MK3')
    _mmmk3 = MaschineMikroMK3()
