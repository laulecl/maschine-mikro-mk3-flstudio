"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	0.1 alpha

    Copyright (c) 2023 Laurent LECLUSE
]]
"""

import Consts
import ui
import midi
import channels


class Daw:

    def __init__(self, router):
        self.router = router

        # list modes by buttons
        self.modeButtons = [Consts.MODE_CHANNEL, Consts.MODE_PLAYLIST, Consts.MODE_PIANO_ROLL, Consts.MODE_MIXER, Consts.MODE_PLUGIN]

        # init mode params
        self.mode = None

    def showModeWindow(self, mode: int = None):
        if mode == Consts.MODE_CHANNEL:
            ui.showWindow(midi.widChannelRack)

        elif mode == Consts.MODE_PLAYLIST:
            ui.showWindow(midi.widPlaylist)

        elif mode == Consts.MODE_PIANO_ROLL:
            ui.showWindow(midi.widPianoRoll)

        elif mode == Consts.MODE_MIXER:
            ui.showWindow(midi.widMixer)

        elif mode == Consts.MODE_PLUGIN:
            channels.showEditor(channels.selectedChannel(), 1)

        self.changeMode(mode)



    def changeMode(self, mode: int = None):
        self.mode = mode
        if mode != None:
            self.router.setBtnPressed(mode, True)
        for b in self.modeButtons:
            if b != mode:
                self.router.setBtnPressed(b, False)



    def updateModes(self):
        wid = ui.getFocusedFormID()
        win = ui.getFocusedFormCaption()

        if wid == midi.widChannelRack and win == 'Channel rack':
            if self.mode != Consts.MODE_CHANNEL:
                self.changeMode(Consts.MODE_CHANNEL)

        elif wid == midi.widPlaylist and win.startswith('Playlist -'):
            if self.mode != Consts.MODE_PLAYLIST:
                self.changeMode(Consts.MODE_PLAYLIST)

        elif wid == midi.widPianoRoll and win.startswith('Piano roll -'):
            if self.mode != Consts.MODE_PIANO_ROLL:
                self.changeMode(Consts.MODE_PIANO_ROLL)

        elif wid == midi.widMixer and win.startswith('Mixer -'):
            if self.mode != Consts.MODE_MIXER:
                self.changeMode(Consts.MODE_MIXER)

        elif ui.getFocusedPluginName() != "":
            if self.mode != Consts.MODE_PLUGIN:
                self.changeMode(Consts.MODE_PLUGIN)

        elif self.mode != None:
            self.changeMode(None)


    def note(self, note: int, octave: int, pressure: int):
        if pressure == 0:
            self.noteOff(note, octave)
        else:
            self.noteOn(note, octave, pressure)


    def noteOn(self, note: int, octave: int, pressure: int):
        index = octave * 12 + note
        channels.midiNoteOn(channels.selectedChannel(), index, pressure)
        #print('note ON : ', index, ', note: ', note, ', octave:',octave, ', pressure: ', pressure)

    def noteOff(self, note: int, octave: int):
        index = octave * 12 + note
        channels.midiNoteOn(channels.selectedChannel(), index, 0)
        #print('note OFF : ', note, ', octave:', octave)