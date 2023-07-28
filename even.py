def even(x):
    return not x or not even (2 * (x < 0) + x - 1)

pee_in_every_pant = (-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5)

print(*map(even, pee_in_every_pant))
