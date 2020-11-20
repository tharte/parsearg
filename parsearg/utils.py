def print_list(x, end='\n'):
    assert isinstance(x, (list, set, map, filter, zip))
    for e in x:
        print(e, end=end)

def is_list_of(x, type=tuple):
    return True if isinstance(x, list) and \
        all(map(lambda x: isinstance(x, type), x)) else False
    
def underline(s, underline_char='-'):
    assert len(underline_char) == 1

    line = underline_char * (len(s)+1)

    return f'{s}:\n{line}'

