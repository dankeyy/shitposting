# https://en.wikipedia.org/wiki/A-Ba-Ni-Bi

import macros

type estring = distinct string


proc beitIt(xs: estring): string {.noinline.} =
  for x in string(xs):
    result &= (if x in "aeiuo": x & "b" & x else: $x)


macro rekt{s}(s: string{lit}): untyped =

  template genStuff(str: untyped): untyped = {.noRewrite.}:
      beitIt(estring(str))

  result = getAst(genStuff(s))


echo "ani ohev otach"

# output:
# abanibi obohebev obotabach
