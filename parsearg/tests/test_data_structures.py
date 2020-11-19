import pytest
from parsearg.data_structures import (
    Fifo,
    Tree,
    is_empty
)

def test_Fifo():
    import collections 
    assert isinstance(Fifo().values, collections.deque)
    assert len(Fifo().values)==0

def test_Fifo_is_empty():
    assert Fifo().is_empty()

def test_Fifo_insert():
    fifo = Fifo()
    fifo.insert('A')
    fifo.insert('B')
    assert fifo.values[0]=='A'
    assert fifo.values[1]=='B'

def test_Fifo_remove():
    fifo = Fifo()
    fifo.insert('A')
    fifo.insert('B')
    assert fifo.remove()=='A'
    assert fifo.remove()=='B'
    assert fifo.is_empty()

def test_Fifo_str():
    fifo = Fifo()
    fifo.insert('A')
    fifo.insert('B')
    assert fifo.__str__()=="deque(['A', 'B'])"


def test_Tree():
    tree = Tree()
    assert tree.value is None
    assert len(tree.children)==0

def test_Tree_is_empty():
    tree = Tree()
    assert tree.is_empty()

def test_is_empty_Tree():
    assert is_empty(None)
    assert is_empty(Tree())

def test_Tree_show():
    s = 'A\n    B\n    BB\n        C\n        CC\n        CCC\n    BBB'

    tree = Tree('A', children=[
        Tree('B', []),
        Tree('BB', children=[
            Tree('C', []), 
            Tree('CC', []), 
            Tree('CCC', [])
        ]),
        Tree('BBB', []),
    ])

    assert tree.show(quiet=True)==s
