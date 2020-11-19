from collections import deque

# TODO: replace with Queue class that accepts a QueueingPolicy class (mixin?)
class Fifo:
    def __init__(self):
        self.values = deque()

    def insert(self, value):
        self.values.append(value)
     
    def remove(self):
        o = self.values.popleft()
        return o

    def is_empty(self):
        return len(self.values) == 0

    def __str__(self):
        return str(self.values)
        

def is_empty(tree):
    assert isinstance(tree, Tree) or tree is None
    return True if tree is None or tree.is_empty() else False

class Tree:
    class Value:
        def __init__(self, name=None, key=None, d=None):
            def check(x):
                if x is not None:
                    assert isinstance(x, str) 
            check(name)
            check(key)

            self.name    = name
            self.key     = key
            if d is not None:
                assert isinstance(d, dict)
                self.payload = d[key]
            else:
                self.payload = d

    def __init__(self, value=None, children=None):
        self.value    = value
        self.children = children if children is not None else []

    def __str__(self):
        return str(self.value)

    def is_empty(self):
        return (self.value is None) and \
               len(self.children) == 0
       
    def show(self, level=0, indent = 4 * ' ', quiet=False):
        # depth-first search (DFS)
        def _show(tree, level, indent):
            nonlocal o
            if is_empty(tree):
                return 

            o += ['{}{}'.format(level*indent, tree)]
            for child in tree.children:
                _show(child, level=level+1, indent=indent)

        o = []
        _show(self, level, indent)
        o = '\n'.join(o)

        if not quiet:
            print(o)

        return o
       
