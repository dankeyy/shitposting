class poop(metaclass=type(
        '_', (type,),
        {
            '__repr__': lambda _: str((f := lambda n: 1 if n <= 2 else f(n - 1) + f(n - 2))(__annotations__['poop'])),
            '__matmul__': lambda _, f: f(_)
        }
)):...

for i in range(1, 10):
    poop : i
    poop @ print

# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
