import sys
import argparse
from unittest.mock import Mock
from collections import deque

def print_list(x, end='\n'):
    assert isinstance(x, (list, set, map, filter, zip))
    for e in x:
        print(e, end=end)

