class C:
    a: int
    b: 'L'
    c: bool
    d: 'M'
    e: tuple
    f: 'A'
    g: str
    h: 'O'


L = "print('like')"
M = "print('share')"
A = "print('subscribe')"
O = "print('hit the bell')"


for poop in C.__annotations__.values():
    @__import__("functools").singledispatch(lambda: None).register
    def _(_) -> poop: pass
