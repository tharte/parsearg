import pytest
from parsearg.utils import (
    is_list_of,
)

def test_is_list_of():
    assert is_list_of([ 'A', 'B', 'C' ], str)
    assert is_list_of([ (None, []) ], tuple)
    assert is_list_of([ [] ], list)

