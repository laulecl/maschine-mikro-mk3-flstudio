"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	1.0

    Copyright (c) 2022 Laurent LECLUSE
]]
"""

import device
import ui
import time
import transport
import mixer
import channels
import midi
import plugins

import Consts


def test(self):
    # plugins.nextPreset(0)
    # ui.hideWindow(midi.widPianoRoll)
    channels.midiNoteOn(0, 40, 127)
    # print('coucou ' + format(device.getPortNumber()))


def printEvent(event, evtype):
    print('----------- NOUVEAU ' + evtype + ' ----------------')
    print("status = " + str(event.status))
    print("data1 = " + str(event.data1))
    print("data2 = " + str(event.data2))
    print("port = " + str(event.port))
    print("note = " + str(event.note))
    print("velocity = " + str(event.velocity))
    print("pressure = " + str(event.pressure))
    print("progNum = " + str(event.progNum))
    print("controlNum = " + str(event.controlNum))
    print("controlVal = " + str(event.controlVal))
    print("pitchBend = " + str(event.pitchBend))
    print("sysex = " + str(event.sysex))
    print("isIncrement = " + str(event.isIncrement))
    print("res = " + str(event.res))
    print("inEv = " + str(event.inEv))
    print("outEv = " + str(event.outEv))
    print("midiId = " + str(event.midiId))
    print("midiChan = " + str(event.midiChan))
    print("midiChanEx = " + str(event.midiChanEx))
    # print("pmeflags = " + str(event.pmeflags))
    print("------- FIN --------")
    print(" ")


def btnName(btn: int):
    return Consts.DEFAULTS[btn]["name"]


"""
presets

ui.previous()
ui.next()


ui.showWindow(midi.widPianoRoll)

Jouer une note...
channels.midiNoteOn(channels.selectedChannel(), 45, 127)

"""
