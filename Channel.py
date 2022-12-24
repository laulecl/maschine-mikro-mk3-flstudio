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



class Context(Context.Abstract):

    # def __init__(self, router):
    #    AbstractContext.__init__(self, router)

    def enabled(self) -> bool:
        return True



    def jog(self, jog: int, mode: int, press: bool, step: int) -> bool:
        if mode == Consts.JOG_VOLUME:
            self.volume(step, press)

        elif mode == Consts.JOG_SWING:
            self.swing(step, press)

        elif mode == Consts.JOG_DEFAULT:
            self.select(step, press)

        else:
            # print("JOG mode=",mode,", press=",press,", step=",step)
            return False

        return True



    def focus(self):
        if not ui.getVisible(midi.widChannelRack):
            ui.showWindow(midi.widChannelRack)

        ui.setFocused(midi.widChannelRack)



    def select(self, step: int, slow: bool):
        nextChannel = channels.selectedChannel() + step
        if nextChannel < 0:
            nextChannel = channels.channelCount() - 1

        if nextChannel > channels.channelCount() - 1:
            nextChannel = 0

        channels.selectOneChannel(nextChannel)



    def add(self):  # todo à implémenter
        return None



    def volume(self, step: int, slow: bool):
        if slow:
            step = 0.01 * step
        else:
            step = 0.02 * step

        volume = channels.getChannelVolume(channels.selectedChannel())
        channels.setChannelVolume(channels.selectedChannel(), volume + step)



    def swing(self, step: int, slow: bool):
        print('swing ', step)
        return None



    def mute(self):
        channels.muteChannel(channels.selectedChannel())



    def solo(self):
        channels.soloChannel(channels.selectedChannel())
