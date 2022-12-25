# name=Native Instruments Maschine Mikro MK3
# supportedHardwareIds=00 20 6B 02 00 04 04 ## Changer
# url=

"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	0.1 alpha

    Copyright (c) 2023 Laurent LECLUSE
]]
"""
import Test
from MaschineMikroMK3 import MaschineMikroMK3



def OnKeyPressure(event):
    global _mmmk3
    _mmmk3.onPadPressure(event)



def OnControlChange(event):
    global _mmmk3
    _mmmk3.onControlChange(event)



def OnUpdateMeters():
    global _mmmk3
    _mmmk3.onGlobalChange()



def OnNoteOn(event):
    event.handled = True



def OnProgramChange(event):
    Test.printEvent(event, "OnProgramChange")



def OnPitchBend(event):
    Test.printEvent(event, "OnPitchBend")



def OnChannelPressure(event):
    Test.printEvent(event, "OnChannelPressure")



def OnSysEx(event):
    Test.printEvent(event, "OnSysEx")



def OnInit():
    global _mmmk3
    print('Loaded MIDI script for Native Instruments Maschine Mikro MK3')
    _mmmk3 = MaschineMikroMK3()
