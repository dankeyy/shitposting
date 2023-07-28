def even(x):
    return not x or not even (((not not x & 2147483648) << 1) - 1 + x)

pee_in_every_pant = (-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5)

print(*map(even, pee_in_every_pant))
