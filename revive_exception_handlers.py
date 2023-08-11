# works only for handlers predefined before the try block
# im not _that_ motivated

def revive_exception_handlers(func):
    import ast, inspect

    class RewriteTry(ast.NodeTransformer):
        def visit_Try(self, node):

            imports = [
                ast.Import(
                        names=[
                            ast.alias(name='_ctypes')
                        ]
                )
            ]

            backups = []
            for handler in node.handlers:
                backups.append(
                    ast.Assign(
                        targets=[
                            ast.Name(id=f'backup_{handler.name}_id', ctx=ast.Store())
                        ],
                        value=ast.Call(
                            func=ast.Name(id='id', ctx=ast.Load()),
                            args=[
                                ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Call(
                                            func=ast.Name(id='locals', ctx=ast.Load()),
                                            args=[],
                                            keywords=[]),
                                        attr='get',
                                        ctx=ast.Load()),
                                    args=[
                                        ast.Constant(value=f'{handler.name}')
                                    ],
                                    keywords=[])
                            ],
                            keywords=[])
                    )
                )

            if backups:
                node.body = imports + backups + node.body

            if not hasattr(node, "finalbody"):
                node.finalbody = []

            assignments = []
            if backups:
                for handler in node.handlers:
                    assignments.append(
                        ast.Assign(
                            targets=[
                                ast.Name(id=handler.name, ctx=ast.Store())],
                                value=ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Name(id='_ctypes', ctx=ast.Load()),
                                        attr='PyObj_FromPtr',
                                        ctx=ast.Load()),
                                    args=[
                                        ast.Name(id=f'backup_{handler.name}_id', ctx=ast.Load())
                                    ],
                                    keywords=[])))
                node.finalbody = assignments + node.finalbody
            return node

    def wrapped(*args, **kwargs):
        import ast
        try:
            tree = ast.parse(inspect.getsource(func))
        except OSError:
            return func(*args, **kwargs)
        tree = ast.parse(inspect.getsource(func))
        tree = ast.fix_missing_locations(RewriteTry().visit(tree))

        print(ast.unparse(tree))
        func.__code__ = compile(tree, '<ast>', 'exec').co_consts[0]
        return func(*args, **kwargs)
    return wrapped


@revive_exception_handlers
def f():
    e = "piss"
    try:
        1 / 0
    except Exception as e:
        ...
    print(e)

f()
