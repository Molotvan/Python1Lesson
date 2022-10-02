from ctypes import sizeof
from os import remove


def convert_int_to_bool(c):
    arr = list(str(bin(c)))
    arr.pop(0)
    arr.pop(0)
    while len(arr) < 3:
        arr.append(0)
    if c <= 3:
        arr = list(reversed(arr))
    return arr


def True_Check(n):
    x = bool(int(convert_int_to_bool(n)[0]))
    y = bool(int(convert_int_to_bool(n)[1]))
    z = bool(int(convert_int_to_bool(n)[2]))
    return not (x or y or z) == (not (x) and not (y) and not (z))


for i in range(0, 8):
    print(i,  True_Check(i))
