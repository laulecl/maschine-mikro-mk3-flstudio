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
import plugins
import channels
import ui
import transport
import midi
import math






class Context(Abstract.Context):

    def enabled(self) -> bool:
        return self.router.daw.mode == Consts.MODE_PLUGIN



    def jog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        if modes & Consts.JOG_DEFAULT and step == 1:
            ui.next()
            # plugins.nextPreset(channels.selectedChannel())
        elif modes & Consts.JOG_DEFAULT and step == -1:
            ui.previous()
            # plugins.prevPreset(channels.selectedChannel())

        elif modes & Consts.JOG_PLUGIN:
            transport.globalTransport(midi.FPT_ChannelJog, step)
            channels.showEditor(channels.selectedChannel(), 1)

        else:
            return False



        return True


    def pad(self, group: int, pad: int, shift: bool, pressure: int):
        if shift:
            return False

        note = (pad-1) % 12
        octave = math.ceil(pad / 12)-1

        self.router.note(note, octave+group-1, pressure)

        return True