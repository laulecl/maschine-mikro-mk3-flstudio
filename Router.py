"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	0.1 alpha

    Copyright (c) 2023 Laurent LECLUSE
]]
"""

import Consts
import Util
import Transport
import Channel
import Pattern
import Grid



class Router:

    def __init__(self, maschineMikroMK3):
        self.mmmk3 = maschineMikroMK3
        self.contexts = [
            Transport.Context(self),
            Channel.Context(self),
            Pattern.Context(self),
            Grid.Context(self)
        ]

        # init jog params
        self.jogModeButtons = [Consts.BTN_VOLUME, Consts.BTN_SWING, Consts.BTN_TEMPO, Consts.BTN_PLUGIN, Consts.BTN_SAMPLING]
        self.jogMode = Consts.JOG_DEFAULT

        # contexts
        self.context = Consts.BTN_SCENE



    def jog(self, jog: int, shift: bool, press: bool, step: int):
        processed = False

        # print("JOG mode=",self.jogMode,", press=",press,", step=",step)
        for context in self.contexts:
            if context.enabled():
                if context.jog(jog, self.jogMode, press, step):
                    processed = True
                    break

        if not processed:
            print('JOG jog=', jog, ", shift=", shift, ", press=", press, ", step=", step, ", jogMode=", self.jogMode)



    def button(self, btn: int, shift: bool, press: bool):
        processed = False

        # BTNs for jog usage
        if Util.inArray(self.jogModeButtons, btn):  # control jog buttons
            if press:
                self.jogMode = btn
            else:
                self.jogMode = Consts.JOG_DEFAULT

            if shift:
                self.jogMode = self.jogMode * -1

            for b in self.jogModeButtons:
                if b != btn:
                    self.setBtnPressed(b, False)

            processed = True
        # BTN jog
        elif btn == Consts.BTN_JOG and press and self.jogMode == None:  # Add pattern, mixer, channel...
            self.dawPattern.add()
            processed = True

        # Other BTNs => LOG
        else:
            for context in self.contexts:
                if context.enabled():
                    if context.button(btn, shift, press):
                        processed = True
                        break

        if not processed:
            print('BUTTON btn=', btn, ", shift=", shift, ", press=", press)



    def pad(self, group: int, pad: int, shift: bool, pressure: int):
        processed = False

        for context in self.contexts:
            if context.enabled():
                if context.pad(group, pad, shift, pressure):
                    processed = True
                    break

        if not processed:
            print('PAD BTN group=', group, ", pad=", pad, ", shift=", shift, ", pressure=", pressure)



    def padChangePressure(self, group: int, pad: int, pressure: int):
        processed = False

        for context in self.contexts:
            if context.enabled():
                if context.padChangePressure(group, pad, pressure):
                    processed = True
                    break

        # if not processed:
        #    print('PAD PRESSURE group=', group, ", pad=", pad, ", pressure=", pressure)



    # usefull shortcut access to low level

    def setBtnPressed(self, btn: int, pressed: bool):
        self.mmmk3.setBtnPressed(btn, pressed)



    def isBtnPressed(self, btn: int):
        return self.mmmk3.isBtnPressed(btn)



    def isPadPressed(self, pad: int):
        return self.mmmk3.isPadPressed(pad)



    def isBtnShifted(self, btn: int):
        return self.mmmk3.isBtnShifted(btn)



    def isPadShifted(self, pad: int):
        return self.mmmk3.isPadShifted(pad)
