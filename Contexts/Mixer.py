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



class Context(Abstract.Context):

    def enabled(self) -> bool:
        return self.router.mode == Consts.MODE_MIXER



    def jog(self, jog: int, modes: int, press: bool, step: int) -> bool:
        if modes & Consts.JOG_DEFAULT:
            transport.globalTransport(midi.FPT_Jog, step)

        elif modes & Consts.JOG_SHIFT:
            transport.globalTransport(midi.FPT_Jog2, step)

        elif modes & Consts.JOG_VOLUME:
            index = mixer.trackNumber()
            value = mixer.getTrackVolume(index)
            if press:
                value = value + step / 200
            else:
                value = value + step / 50
            mixer.setTrackVolume(index, value)

        elif modes & Consts.JOG_POSITION:
            index = mixer.trackNumber()
            value = mixer.getTrackPan(index)
            if press:
                value = value + step / 200
            else:
                value = value + step / 50
            mixer.setTrackPan(index, value)

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

