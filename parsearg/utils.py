import sys
import argparse
from unittest.mock import Mock
from collections import deque

def print_list(x, end='\n'):
    assert isinstance(x, (list, set, map, filter, zip))
    for e in x:
        print(e, end=end)

def is_list_of(x, type=tuple):
    return True if isinstance(x, list) and \
        all(map(lambda x: isinstance(x, type), x)) else False
    
