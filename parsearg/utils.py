from types import FunctionType

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

def is_argument_field(field):
    # Is field a legitimate ArgumentParser.add_argument argument?
    #
    # Source:
    #     https://python.readthedocs.io/en/stable/library/argparse.html#the-add-argument-method

    assert isinstance(field, str)

    fields = [
        # [str]: name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
        'action',    #  - The basic type of action to be taken when this argument is encountered at the command line.
        'nargs',     #  - The number of command-line arguments that should be consumed.
        'const',     #  - A constant value required by some action and nargs selections.
        'default',   #  - The value produced if the argument is absent from the command line.
        'type',      #  - The type to which the command-line argument should be converted.
        'choices',   #  - A container of the allowable values for the argument.
        'required',  #  - Whether or not the command-line option may be omitted (optionals only).
        'help',      #  - A brief description of what the argument does.
        'metavar',   #  - A name for the argument in usage messages.
        'dest',      #  - The name of the attribute to be added to the object returned by parse_args().
    ]

    return field in fields 

