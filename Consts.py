"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	0.1 alpha

    Copyright (c) 2023 Laurent LECLUSE
]]
"""

BTN_PROJECT = 38
BTN_FAVORITE = 39
BTN_BROWSER = 40

BTN_JOG = 8
BTN_VOLUME = 44
BTN_PLUGIN = 45
BTN_SWING = 46
BTN_SAMPLING = 47
BTN_TEMPO = 48

BTN_PITCH = 49
BTN_MOD = 50
BTN_PERFORM = 51
BTN_NOTES = 52

BTN_AUTO = 35
BTN_LOCK = 36
BTN_NOTE_REPEAT = 37

BTN_RESTART = 53
BTN_ERASE = 54
BTN_TAP = 55
BTN_FOLLOW = 56
BTN_PLAY = 57
BTN_REC = 58
BTN_STOP = 59

BTN_FIXED_VEL = 80
BTN_PAD_MODE = 81
BTN_KEYBOARD = 82
BTN_CHORDS = 84
BTN_STEP = 83
BTN_SCENE = 85
BTN_PATTERN = 86
BTN_EVENTS = 87
BTN_VARIATION = 88
BTN_DUPLICATE = 89
BTN_SELECT = 90
BTN_SOLO = 91
BTN_MUTE = 92

PAD_UNDO = 1
PAD_REDO = 2
PAD_STEP_UNDO = 3
PAD_STEP_REDO = 4
PAD_QUANTIZE = 5
PAD_QUANTIZE_50P = 6
PAD_NUDGE_LEFT = 7
PAD_NUDGE_RIGHT = 8
PAD_CLEAR = 9
PAD_CLEAR_AUTO = 10
PAD_COPY = 11
PAD_PASTE = 12
PAD_SEMITONE_MINUS = 13
PAD_SEMITONE_PLUS = 14
PAD_OCTAVE_MINUS = 15
PAD_OCTAVE_PLUS = 16

JOG_DEFAULT = 0b00000000001
JOG_SHIFT = 0b00000000010
JOG_VOLUME = 0b00000000100
JOG_VELOCITY = 0b00000001000
JOG_SWING = 0b00000010000
JOG_POSITION = 0b00000100000
JOG_TEMPO = 0b00001000000
JOG_TUNE = 0b00010000000
JOG_PLUGIN = 0b00100000000
JOG_MACRO = 0b01000000000
JOG_SAMPLING = 0b10000000000

GRID_NOTE = 60
GRID_VELOCITY = 100

MODE_CHANNEL = BTN_SCENE
MODE_PLAYLIST = BTN_PATTERN
MODE_PIANO_ROLL = BTN_EVENTS
MODE_MIXER = BTN_VARIATION
MODE_PLUGIN = BTN_SELECT

NOTE_DO = 0
NOTE_DO2 = 1
NOTE_RE = 2
NOTE_RE2 = 3
NOTE_MI = 4
NOTE_FA = 5
NOTE_FA2 = 6
NOTE_SOL = 7
NOTE_SOL2 = 8
NOTE_LA = 9
NOTE_LA2 = 10
NOTE_SI = 11


DEFAULTS = {
    BTN_PROJECT:     {
        "name":    "PROJECT",
        "pressed": False
    },
    BTN_FAVORITE:    {
        "name":    "FAVORITE",
        "pressed": False
    },
    BTN_BROWSER:     {
        "name":    "BROWSER",
        "pressed": False
    },
    BTN_JOG:         {
        "name":    "JOG",
        "pressed": False
    },
    BTN_VOLUME:      {
        "name":    "VOLUME",
        "pressed": False
    },
    BTN_PLUGIN:      {
        "name":    "PLUGIN",
        "pressed": False
    },
    BTN_SWING:       {
        "name":    "SWING",
        "pressed": False
    },
    BTN_SAMPLING:    {
        "name":    "SAMPLING",
        "pressed": False
    },
    BTN_TEMPO:       {
        "name":    "TEMPO",
        "pressed": False
    },
    BTN_PITCH:       {
        "name":    "PITCH",
        "pressed": False
    },
    BTN_MOD:         {
        "name":    "MOD",
        "pressed": False
    },
    BTN_PERFORM:     {
        "name":    "PERFORM",
        "pressed": False
    },
    BTN_NOTES:       {
        "name":    "NOTES",
        "pressed": False
    },
    BTN_AUTO:        {
        "name":    "AUTO",
        "pressed": False
    },
    BTN_LOCK:        {
        "name":    "LOCK",
        "pressed": False
    },
    BTN_NOTE_REPEAT: {
        "name":    "NOTE_REPEAT",
        "pressed": False
    },
    BTN_RESTART:     {
        "name":    "RESTART",
        "pressed": False
    },
    BTN_ERASE:       {
        "name":    "ERASE",
        "pressed": False
    },
    BTN_TAP:         {
        "name":    "TAP",
        "pressed": False
    },
    BTN_FOLLOW:      {
        "name":    "FOLLOW",
        "pressed": False
    },
    BTN_PLAY:        {
        "name":    "PLAY",
        "pressed": False
    },
    BTN_REC:         {
        "name":    "REC",
        "pressed": False
    },
    BTN_STOP:        {
        "name":    "STOP",
        "pressed": False
    },
    BTN_FIXED_VEL:   {
        "name":    "FIXED_VEL",
        "pressed": False
    },
    BTN_PAD_MODE:    {
        "name":    "PAD_MODE",
        "pressed": False
    },
    BTN_KEYBOARD:    {
        "name":    "KEYBOARD",
        "pressed": False
    },
    BTN_CHORDS:      {
        "name":    "CHORDS",
        "pressed": False
    },
    BTN_STEP:        {
        "name":    "STEP",
        "pressed": False
    },
    BTN_SCENE:       {
        "name":    "SCENE",
        "pressed": False
    },
    BTN_PATTERN:     {
        "name":    "PATTERN",
        "pressed": False
    },
    BTN_EVENTS:      {
        "name":    "EVENTS",
        "pressed": False
    },
    BTN_VARIATION:   {
        "name":    "VARIATION",
        "pressed": False
    },
    BTN_DUPLICATE:   {
        "name":    "DUPLICATE",
        "pressed": False
    },
    BTN_SELECT:      {
        "name":    "SELECT",
        "pressed": False
    },
    BTN_SOLO:        {
        "name":    "SOLO",
        "pressed": False
    },
    BTN_MUTE:        {
        "name":    "MUTE",
        "pressed": False
    },
}
