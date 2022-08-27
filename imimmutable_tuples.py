from ctypes import py_object, byref, pythonapi

A = py_object(('get',) * 257)

print(A.value)
print(id(A.value))

pythonapi._PyTuple_Resize(byref(A), 1)
pythonapi.PyTuple_SetItem(A, 0, py_object('rekt'))

print(A.value)
print(id(A.value))

# output:
# ('get', 'get', 'get', 'get', 'get', 'get', 'get', ... )
# 93911217660720
# ('rekt',)
# 93911217660720
