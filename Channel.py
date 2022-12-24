"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	0.1 alpha

    Copyright (c) 2023 Laurent LECLUSE
]]
"""

import Context
import Consts
import channels
import general
import midi
import transport
import ui



class Context(Context.Abstract):

    # def __init__(self, router):
    #    AbstractContext.__init__(self, router)

    def enabled(self) -> bool:
        return ui.getFocusedFormID() == midi.widChannelRack



    def button(self, btn: int, shift: bool, press: bool) -> bool:
        if btn == Consts.BTN_SOLO:
            channels.soloChannel(channels.selectedChannel())

        elif btn == Consts.BTN_MUTE:
            channels.muteChannel(channels.selectedChannel())

        else:
            return False

        return True



    def jog(self, jog: int, mode: int, press: bool, step: int) -> bool:
        if mode == Consts.JOG_VOLUME:
            self.volume(step, press)

        elif mode == Consts.JOG_SWING:
            value = general.processRECEvent(midi.REC_Chan_SwingMix, 0, midi.REC_GetValue)
            general.processRECEvent(midi.REC_Chan_SwingMix, value + step, midi.REC_Control)

        else:
            return False

        return True



    def focus(self):
        if not ui.getVisible(midi.widChannelRack):
            ui.showWindow(midi.widChannelRack)

        ui.setFocused(midi.widChannelRack)



    def add(self):  # todo à implémenter
        return None



    def volume(self, step: int, slow: bool):
        if slow:
            step = 0.01 * step
        else:
            step = 0.02 * step

        volume = channels.getChannelVolume(channels.selectedChannel())
        channels.setChannelVolume(channels.selectedChannel(), volume + step)
