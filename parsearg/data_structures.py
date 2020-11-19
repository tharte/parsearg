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
        

class Tree:
    def __init__(self, value=None, children=None):
        self.value    = value
        self.children = children if children is not None else []

    def __str__(self):
        return str(self.value)

    def is_empty(self):
        return (self.value is None) and \
               len(self.children) == 0
       
