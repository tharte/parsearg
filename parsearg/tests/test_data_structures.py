import pytest
from parsearg.data_structures import (
    Fifo,
    Tree,
    is_empty,
    Node,
    Key,
)
from parsearg.utils import (
    is_list_of,
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

def test_Tree_Value():
    value = Tree.Value()
    assert value.name is None
    assert value.key is None
    assert value.payload is None

    d = {
        'A|B|C': {
            'arg1': {},
            'arg2': {},
            'arg3': {},
        }
    }

    value = Tree.Value(name='C', key=set(d.keys()).pop(), d=d)

    assert value.name=='C'
    assert value.key=='A|B|C'
    assert value.payload==d['A|B|C']


def test_Node():
    node = Node()
    assert Node().value==(None, [])

    node = Node(head='A', tail=['B', ['C']])
    assert node.value == ('A', ['B', ['C']])

def test_Node_head():
    node = Node(head='A', tail=['B', ['C']])
    assert node.head() == 'A' 

def test_Node_tail():
    node = Node(head='A', tail=['B', ['C']])
    assert node.tail() == ['B', ['C']]

def test_Node_is_empty():
    assert Node().is_empty()
    assert not Node('A').is_empty() 
    assert not Node('A', []).is_empty() 

def test_Node_lsfhift():
    node = Node(head='A', tail=['B', ['C']])
    assert (node << 1).head() == 'B'
    assert (node << 2).head() == 'C'

def test_Node_eq():
    assert Node() == Node()
    assert Node('A') == Node('A', [])

def test_Node_from_nested_list():
    # e.g. split from key:
    #     'A|B|C' -> ['A', '|', 'B', '|', 'C'] -> ['A', ['B', ['C']]]
    ll = ['A', ['B', ['C']]]
    assert Node.from_nested_list(ll) == Node(head='A', tail=['B', ['C']])


def test_Key():
    key = Key()
    assert key.key is None
    assert key.value == Node()
    assert key.payload is None

