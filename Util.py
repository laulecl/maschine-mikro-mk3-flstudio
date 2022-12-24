"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	1.0

    Copyright (c) 2022 Laurent LECLUSE
]]
"""



def inArray(haystack, needle):
    for n in haystack:
        if n == needle:
            return True
    return False
