
class IntEnum:
    pass

class Enum:
    pass

class _Auto:
    def __init__(self):
        self._i = -1
    def __call__(self):
        self._i += 1
        return self._i

auto = _Auto()
