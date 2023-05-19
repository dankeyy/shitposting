import ctypes

class poo(dict):
    def __missing__(self, name):
        try:
            return __builtins__.eval(name)
        except:
            return name
    __slots__ = ()

ctypes.py_object.from_address(id(locals()) + 8).value=poo

for i in (lol, kek, lmao):
    print(i)
