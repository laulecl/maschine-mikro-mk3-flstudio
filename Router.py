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
from DawPattern import DawPattern



class Router:

    def __init__(self, maschineMikroMK3):
        self.mmmk3 = maschineMikroMK3
        self.contexts = {
            Consts.CONTEXT_TRANSPORT: Transport.Context(self),
            Consts.CONTEXT_CHANNEL: Channel.Context(self)
        }

        self.dawPattern = DawPattern()

        # init jog params
        self.jogModeButtons = [Consts.BTN_VOLUME, Consts.BTN_SWING, Consts.BTN_TEMPO, Consts.BTN_PLUGIN, Consts.BTN_SAMPLING]
        self.jogMode = Consts.JOG_DEFAULT

        # contexts
        self.context = Consts.BTN_SCENE



    def jog(self, jog: int, shift: bool, press: bool, step: int):
        # print("JOG mode=",self.jogMode,", press=",press,", step=",step)
        for c in self.contexts:
            if self.contexts[c].enabled():
                if self.contexts[c].jog(jog, self.jogMode, press, step):
                    break



    def button(self, btn: int, shift: bool, press: bool):
        # BTN PROJECT
        if btn == Consts.BTN_PROJECT and press:
            return None

        # BTN FAVORITE
        elif btn == Consts.BTN_FAVORITE:
            return None

        # BTN BROWSER
        elif btn == Consts.BTN_BROWSER:
            self.dawTransport.browser()

        # BTNs for jog usage
        elif Util.inArray(self.jogModeButtons, btn):  # control jog buttons
            if press:
                self.jogMode = btn
            else:
                self.jogMode = Consts.JOG_DEFAULT

            if shift:
                self.jogMode = self.jogMode * -1

            for b in self.jogModeButtons:
                if b != btn:
                    self.setBtnPressed(b, False)

        # BTN jog
        elif btn == Consts.BTN_JOG and press and self.jogMode == None:  # Add pattern, mixer, channel...
            self.dawPattern.add()

        # BTN TAP / METRO
        elif btn == Consts.BTN_TAP and press:
            # todo attention à l'éclairage du bouton
            if not shift:
                self.dawTransport.tapTempo()
            else:
                self.dawTransport.metronome()

        # BTN PLAY
        elif btn == Consts.BTN_PLAY and press:
            if shift:
                self.dawTransport.playMode()
            self.dawTransport.play()

        # BTN REC
        elif btn == Consts.BTN_REC:
            self.dawTransport.record()

        # BTN STOP
        elif btn == Consts.BTN_STOP and press:
            self.dawTransport.stop()

        # Other BTNs => LOG
        else:
            for c in self.contexts:
                if self.contexts[c].enabled():
                    if self.contexts[c].button(btn, shift, press):
                        break



    def pad(self, group: int, pad: int, shift: bool, pressure: int):
        if False:
            return None

        # Other cases => LOG
        else:
            # print('PAD group=' + str(group) + ", pad=" + str(pad) + ", shift=" + str(shift) + ", pressure=" + str(pressure))
            for c in self.contexts:
                if self.contexts[c].enabled():
                    if self.contexts[c].pad(group, pad, shift, pressure):
                        break



    def padChangePressure(self, group: int, pad: int, pressure: int):
        if False:
            return None
        # print('PAD CHANGE PRESSURE group=' + str(group) + ", pad=" + str(pad) + ", pressure=" + str(pressure))
        else:
            # print('PAD group=' + str(group) + ", pad=" + str(pad) + ", shift=" + str(shift) + ", pressure=" + str(pressure))
            for c in self.contexts:
                if self.contexts[c].enabled():
                    if self.contexts[c].pad(group, pad, shift, pressure):
                        break



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
