from ctypes import cast, POINTER, c_int

cast(id(False), POINTER(c_int))[4] = 1
cast(id(False), POINTER(c_int))[6] = 1

print(True == False) 
# True
