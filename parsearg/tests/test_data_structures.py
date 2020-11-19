import pytest
from parsearg.data_structures import Fifo

def test_Fifo():
    import collections 
    assert isinstance(Fifo().values, collections.deque)
    assert len(Fifo().values)==0


