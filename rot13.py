import ast
import sysconfig

with open(sysconfig.get_paths()['stdlib'] + '/this.py') as f:
    txt = f.read()

a = ast.parse(txt)
a.body[0].value.value = input()
exec(compile(a, '<string>', 'exec'))

# /stdin yznb -> lmao
