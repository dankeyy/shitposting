from ctypes import cast, py_object

x = 'kek'

f = cast(id(None) + 15904, py_object).value(compile('print(x)', '', 'single'), globals())

print(f)
# <function __main__.<module>()>

f()
# kek
