import functools
import inspect

# helpers
eprint = functools.partial(print, end='\n---------------------\n')

def raw(string):
    return string.replace('"', r'\"')

def _parens(code):
    opening = closing = 0
    marks = []

    for i, v in enumerate(code):
        if code[i-1] != '\\':

            if v in ("'", '"'):
                marks.append(v)

            elif marks and marks[-1] == v:
                marks.pop()

                if not marks:
                    return i

            if len(marks) != 1:
                if   v == '(': opening += 1
                elif v == ')': closing += 1

            if closing > opening:
                return i


def myargs_repr():
    func_name = inspect.stack()[1][3]
    parent_frame = inspect.stack()[2][0]
    lineo = parent_frame.f_lineno-1
    upper_frame = parent_frame
    while upper_frame.f_back:
        upper_frame = upper_frame.f_back

    code = inspect.getsource(upper_frame)

    # seek beginning of function call by traversing the code until call line
    line = p = 0
    while line != lineo:
        if code[p] == '\n':
            line += 1
        p += 1

    # slice the code
    # from beginning of call (after opening paren)
    # up until the last relevant closing paren
    code = code[p:]
    code = code[code.index(func_name) + len(func_name) + 1:]
    code = code[:_parens(code)] # _parens might return None but that's ok, [:None] is valid

    # code is now a repr of the function call arguments
    return code


def f(*args):
    return myargs_repr()


eprint()


assert f("(") == "\"(\""
assert f("foo'bar") == "\"foo'bar\"", f("foo'bar")
assert f("foo\"bar") == r'''"foo\"bar"'''
assert f('foo\"bar') == r"'foo\"bar'"
assert f("foo\"bar(") == r'"foo\"bar("'


eprint(f("    ("
         ))

cool = 2
eprint(f(cool))


banana = 2
eprint(
    f(
        banana,
        lambda: 1,
        (lambda: 2)(),
        object(),
        1,
        2
    ),
)

def g():
    eprint(f(
    "from g scope"
            )
    )

g()

eprint(f(
    1,
        2
))


# some more sane tests
def g():
    assert f(banana, 2) == "banana, 2", f(banana, 2)
    assert f(2) == "2"
g()


assert f((lambda: 1)())  == "(lambda: 1)()"
assert f((1,2, 3))  == "(1,2, 3)"
assert f( [1,2,3] )  == " [1,2,3] "
assert f("banana") == "\"banana\""


# output:
# ---------------------
# "    ("
#
# ---------------------
# cool
# ---------------------
#
#         banana,
#         lambda: 1,
#         (lambda: 2)(),
#         object(),
#         1,
#         2
#
# ---------------------
#
#    "from g scope"
#
# ---------------------
#
#     1,
#         2
#
# ---------------------
