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
import patterns
import transport
import midi
import mixer
import ui



class Context(Abstract.Context):

    def enabled(self) -> bool:
        return ui.getFocusedFormID() == midi.widMixer



    def jog(self, jog: int, mode: int, press: bool, step: int) -> bool:
        if False:
            pass

        #elif mode == Consts.JOG_VOLUME:


        else:
            return False

        return True



    def button(self, btn: int, shift: bool, press: bool) -> bool:
        if btn == Consts.BTN_SOLO:
            mixer.soloTrack(mixer.trackNumber())

        elif btn == Consts.BTN_MUTE:
            mixer.muteTrack(mixer.trackNumber())

        else:
            return False

        return True

