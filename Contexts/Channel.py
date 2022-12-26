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
import channels
import general
import midi
import transport
import ui



class Context(Abstract.Context):

    # def __init__(self, router):
    #    AbstractContext.__init__(self, router)

    def enabled(self) -> bool:
        return self.router.mode == Consts.MODE_CHANNEL



    def button(self, btn: int, shift: bool, press: bool) -> bool:
        if btn == Consts.BTN_SOLO:
            channels.soloChannel(channels.selectedChannel())

        elif btn == Consts.BTN_MUTE:
            channels.muteChannel(channels.selectedChannel())

        else:
            return False

        return True



    def jog(self, jog: int, modes: int, press: bool, step: int) -> bool:

        if modes & Consts.JOG_DEFAULT:
            transport.globalTransport(midi.FPT_ChannelJog, step)

        elif modes & Consts.JOG_SHIFT:
            transport.globalTransport(midi.FPT_PatternJog, step)

        elif modes & Consts.JOG_VOLUME:
            self.changeParameter(midi.REC_Chan_Vol, step, press)

        elif modes & Consts.JOG_SWING:
            self.changeParameter(midi.REC_Chan_SwingMix, step, press)

        elif modes & Consts.JOG_POSITION:
            self.changeParameter(midi.REC_Chan_Pan, step, press)

        else:
            return False

        return True



    def focus(self):
        if not ui.getVisible(midi.widChannelRack):
            ui.showWindow(midi.widChannelRack)

        ui.setFocused(midi.widChannelRack)



    def add(self):  # todo à implémenter
        return None



    def changeParameter(self, recEvent: int, step: int, slow: bool):
        eventId = recEvent + channels.getRecEventId(channels.selectedChannel())
        newValue = channels.incEventValue(eventId, step)
        general.processRECEvent(eventId, newValue, midi.REC_UpdateValue | midi.REC_UpdateControl)
