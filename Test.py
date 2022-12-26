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
import playlist
import general

import Consts



def test():
    #pindex = 1
    #pvalue = 1

    #print(plugins.getParamName(pindex, channels.selectedChannel()))
    #plugins.setParamValue(pvalue, pindex, channels.selectedChannel())

    #transport.globalTransport(midi.FPT_StepEdit, 1)

    pass


def testJog(step: int):
    #length = transport.getSongLength(midi.SONGLENGTH_S)

    pos = transport.getSongPos(midi.SONGLENGTH_ABSTICKS)
    pos += step * 384
    transport.setSongPos(pos, midi.SONGLENGTH_ABSTICKS)







def printPlugin():
    index = channels.selectedChannel()
    if not plugins.isValid(index):
        return None

    print( "Nom du plugin:",plugins.getPluginName(index) )
    print("Index du plugin:", index)
    print("Nombre de paramètres:", plugins.getParamCount(index))
    for p in range(plugins.getParamCount(index)):
        pname = plugins.getParamName(p, index)
        pvalue = plugins.getParamValue(p, index)
        if pname != "" and pname != "#"+str(p).ljust(3,'0'):
            print(str(p).ljust(5, ' '), pname.ljust(50, ' '), pvalue)



def printEvent(event, evtype=""):
    nameLength = 15
    valLength = 15

    # res HIDDEN

    print('\u250C' + '\u2500MIDI\u2500EVENT\u2500\u2500\u2500\u2500' + str(evtype).ljust(22, '\u2500') + str('').rjust(20, '\u2500') + '\u2510')

    print(_eventAttr("status", str(event.status)) + _eventAttr("midiId", str(event.midiId)) + "\u2502")
    print(_eventAttr("data1", str(event.data1)) + _eventAttr("controlNum", str(event.controlNum)) + "\u2502")
    print(_eventAttr("data2", str(event.data2)) + _eventAttr("controlVal", str(event.controlVal)) + "\u2502")
    print(_eventAttr("port", str(event.port)) + _eventAttr("isIncrement", str(event.isIncrement)) + "\u2502")
    print(_eventAttr("note", str(event.note)) + _eventAttr("progNum", str(event.progNum)) + "\u2502")
    print(_eventAttr("velocity", str(event.velocity)) + _eventAttr("pressure", str(event.pressure)) + "\u2502")
    print(_eventAttr("pitchBend", str(event.pitchBend)) + _eventAttr("sysex", str(event.sysex)) + "\u2502")
    print(_eventAttr("inEv", str(event.inEv)) + _eventAttr("midiChanEx", str(event.midiChanEx)) + "\u2502")
    print(_eventAttr("outEv", str(event.outEv)) + _eventAttr("midiChan", str(event.midiChan)) + "\u2502")

    print("\u2514" + str("").rjust(57, "\u2500") + "\u2518")
    print(" ")



def _eventAttr(name: str, value: str):
    return "\u2502 " + name.ljust(11, ' ') + " = " + value.rjust(12, ' ') + ' '



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
