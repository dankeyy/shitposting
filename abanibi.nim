# https://en.wikipedia.org/wiki/A-Ba-Ni-Bi

import macros

macro rekt{str}(str: string{lit}): untyped =

  template beitIt(str: string): string = {.noRewrite.}:
    var s = ""
    for c in str:
      s &= (
            if c in "aeiuo":
              c & "b" & c
            else:
              $c
      )
    s

  result = getAst(beitIt(str))


echo "ani ohev otach"

# output:
# abanibi obohebev obotabach
