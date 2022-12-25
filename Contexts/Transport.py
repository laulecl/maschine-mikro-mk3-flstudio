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
import transport
import midi



class Context(Abstract.Context):

    def enabled(self) -> bool:
        return True



    def jog(self, jog: int, mode: int, press: bool, step: int) -> bool:
        if mode == Consts.JOG_POSITION:
            self.trackPos(step, press)

        elif mode == Consts.JOG_TEMPO:
            self.tempo(step, press)

        else:
            return False

        return True



    def button(self, btn: int, shift: bool, press: bool) -> bool:
        if btn == Consts.BTN_TAP:
            if not shift:  # TAP Tempo
                transport.globalTransport(midi.FPT_TapTempo, 1)
            else:  # toggle metronome
                transport.globalTransport(midi.FPT_Metronome, 1)

        elif btn == Consts.BTN_PLAY:
            if shift:
                transport.setLoopMode()
            else:
                transport.start()

        elif btn == Consts.BTN_REC:
            transport.record()

        elif btn == Consts.BTN_STOP:
            transport.stop()

        else:
            return False

        return True



    def trackPos(self, step: int, slow: bool):
        # todo bug de positionnement
        step = step * 10
        if not slow:
            step = step * 100

        # print(str(transport.getSongPos(midi.SONGLENGTH_MS)))
        transport.setSongPos(transport.getSongPos(midi.SONGLENGTH_MS) + step, midi.SONGLENGTH_MS)



    def tempo(self, step: int, slow: bool):
        if not slow:
            step = step * 10

        transport.globalTransport(midi.FPT_TempoJog, step)
