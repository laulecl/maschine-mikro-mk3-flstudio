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
import Util
import Loader
import Daw
import ui
import midi
import channels



class Router:

    def __init__(self, maschineMikroMK3):
        self.device = maschineMikroMK3
        self.daw = Daw.Daw(self)
        self.loader = Loader.Loader(self)

        self.jogModes = Consts.JOG_DEFAULT




    def jog(self, jog: int, shift: bool, press: bool, step: int):
        processed = False
        self._jogBtnPress(Consts.BTN_RESTART, press, shift)

        if self.isBtnPressed(Consts.BTN_PROJECT):  # just for tests!!!
            Test.testJog(step)
            return True

        for context in self.loader.contexts():
            if context.enabled():
                if context.jog(jog, self.jogModes, press, step):
                    processed = True
                    break

        if not processed:
            print('JOG jog=', jog, ", step=", step, ", press=", press, ", modes=", self._jogModesStr())



    def button(self, btn: int, shift: bool, press: bool):
        processed = False

        # experimental, need bo be removed
        if btn == Consts.BTN_PROJECT and press:
            Test.test()
            processed = True

        # Jog btns
        elif btn in [Consts.BTN_VOLUME, Consts.BTN_PLUGIN, Consts.BTN_SWING, Consts.BTN_SAMPLING, Consts.BTN_TEMPO]:
            self._jogBtnPress(btn, shift, press)
            processed = True

        # BTNs for window switch mode usage
        elif btn in self.daw.modeButtons:
            self.daw.showModeWindow(btn)
            processed = True

        # Other BTNs
        else:
            for context in self.loader.contexts():
                if context.enabled():
                    if context.button(btn, shift, press):
                        processed = True
                        break

        if not processed:
            print('BUTTON btn=', btn, ", shift=", shift, ", press=", press)



    def pad(self, group: int, pad: int, shift: bool, pressure: int):
        processed = False

        for context in self.loader.contexts():
            if context.enabled():
                if context.pad(group, pad, shift, pressure):
                    processed = True
                    break

        if not processed:
            print('PAD BTN group=', group, ", pad=", pad, ", shift=", shift, ", pressure=", pressure)



    def padChangePressure(self, group: int, pad: int, pressure: int):
        processed = False

        for context in self.loader.contexts():
            if context.enabled():
                if context.padChangePressure(group, pad, pressure):
                    processed = True
                    break

         #if not processed:
         #   print('PAD PRESSURE group=', group, ", pad=", pad, ", pressure=", pressure)



    def _jogBtnPress(self, btn: int, shift: bool, state: bool):

        if btn == Consts.BTN_RESTART:
            jogMode = Consts.JOG_SHIFT
        elif btn == Consts.BTN_VOLUME and not shift:
            jogMode = Consts.JOG_VOLUME
        elif btn == Consts.BTN_VOLUME and shift:
            jogMode = Consts.JOG_VELOCITY
        elif btn == Consts.BTN_PLUGIN and not shift:
            jogMode = Consts.JOG_PLUGIN
        elif btn == Consts.BTN_PLUGIN and shift:
            jogMode = Consts.JOG_MACRO
        elif btn == Consts.BTN_SWING and not shift:
            jogMode = Consts.JOG_SWING
        elif btn == Consts.BTN_SWING and shift:
            jogMode = Consts.JOG_POSITION
        elif btn == Consts.BTN_SAMPLING:
            jogMode = Consts.JOG_SAMPLING
        elif btn == Consts.BTN_TEMPO and not shift:
            jogMode = Consts.JOG_TEMPO
        elif btn == Consts.BTN_TEMPO and shift:
            jogMode = Consts.JOG_TUNE
        else:
            return True

        if state:
            self.jogModes = self.jogModes & ~Consts.JOG_DEFAULT
            self.jogModes = self.jogModes | jogMode

        else:
            self.jogModes = self.jogModes & ~jogMode
            if self.jogModes == 0: self.jogModes = Consts.JOG_DEFAULT



    def _jogModesStr(self) -> str:
        res = ""
        if self.jogModes & Consts.JOG_DEFAULT: res += "DEFAULT,"
        if self.jogModes & Consts.JOG_SHIFT: res += "SHIFT,"
        if self.jogModes & Consts.JOG_VOLUME: res += "VOLUME,"
        if self.jogModes & Consts.JOG_VELOCITY: res += "VELOCITY,"
        if self.jogModes & Consts.JOG_SWING: res += "SWING,"
        if self.jogModes & Consts.JOG_POSITION: res += "POSITION,"
        if self.jogModes & Consts.JOG_TEMPO: res += "TEMPO,"
        if self.jogModes & Consts.JOG_TUNE: res += "TUNE,"
        if self.jogModes & Consts.JOG_PLUGIN: res += "PLUGIN,"
        if self.jogModes & Consts.JOG_MACRO: res += "MACRO,"
        if self.jogModes & Consts.JOG_SAMPLING: res += "SAMPLING,"
        return res[:-1]


    # usefull shortcut access to device or daw
    def setBtnPressed(self, btn: int, pressed: bool):
        self.device.setBtnPressed(btn, pressed)

    def isBtnPressed(self, btn: int) -> bool:
        return self.device.isBtnPressed(btn)

    def isPadPressed(self, pad: int) -> bool:
        return self.device.isPadPressed(pad)

    def isBtnShifted(self, btn: int) -> bool:
        return self.device.isBtnShifted(btn)

    def isPadShifted(self, pad: int) -> bool:
        return self.device.isPadShifted(pad)

    def note(self, note: int, octave: int, pressure: int):
        self.daw.note(note,octave, pressure)

    def noteOn(self, note: int, octave: int, pressure: int):
        self.daw.noteOn(note, octave, pressure)

    def noteOff(self, note: int, octave: int):
        self.daw.noteOff(note, octave)