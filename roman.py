def roman(n): 
    return next((l + roman(n-c) for c, l in zip([1000, 900, 500, 400,  100,  90,  50,  40,   10,   9,    5,   4,    1 ], ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]) if c <= n), '')

print(roman(420))
