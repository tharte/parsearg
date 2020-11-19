import pytest
from parsearg.data_structures import Fifo

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
