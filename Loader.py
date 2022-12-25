"""
[[
	Surface:	Maschine Mikro MK3
	Developer:	Laurent LECLUSE
	Version:	0.1 alpha

    Copyright (c) 2023 Laurent LECLUSE
]]
"""

import Contexts.Transport
import Contexts.Channel
import Contexts.Pattern
import Contexts.Grid
import Contexts.Mixer
import Plugins.FlKeys



class Loader:

    def __init__(self, router):
        self._contexts = [
            Contexts.Transport.Context(router),

            Plugins.FlKeys.Plugin(router),

            Contexts.Channel.Context(router),
            Contexts.Pattern.Context(router),
            Contexts.Grid.Context(router),
            Contexts.Mixer.Context(router)
        ]

    def contexts(self):
        return self._contexts
