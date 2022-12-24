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
import transport
import midi


class Context(Context.Abstract):

    def enabled(self) -> bool:
        return True

    def jog(self, jog: int, mode: int, press: bool, step: int) -> bool:
        if mode == Consts.JOG_POSITION:
            self.trackPos(step, press)

        elif mode == Consts.JOG_TEMPO:
            self.tempo(step, press)

        else:
            # print("JOG mode=",mode,", press=",press,", step=",step)
            return False

        return True






    def browser(self):
        transport.globalTransport(midi.FPT_F8, 1)

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

    def tapTempo(self):
        transport.globalTransport(midi.FPT_TapTempo, 1)

    def metronome(self):
        transport.globalTransport(midi.FPT_Metronome, 1)

    def playMode(self):
        print("DawGlobal.playMode")

    def play(self):
        transport.start()

    def record(self):
        transport.record()

    def stop(self):
        transport.stop()
