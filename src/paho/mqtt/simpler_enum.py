class SimplerEnum:
    pass

class Enum(SimplerEnum):
    pass

IntEnum = Enum

class _Auto:
    def __init__(self):
        self._i = -1
    def __call__(self):
        self._i += 1
        return self._i

auto = _Auto()