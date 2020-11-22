import pytest 
import argparse
from parsearg.data_structures import (
    Tree,
)

from unittest.mock import Mock

m = Mock()

def make_callback(name):
    mm = Mock()
    mm.configure_mock(**{'method': name})

    def func(args):
        if isinstance(args, argparse.Namespace):
            args = {k:v for k, v in args.__dict__.items() if k != 'callback'}

        a = f'args: {args!r}'

        m.attach_mock(mm, name)
        o = '\t{}\n\t{}'.format(a, getattr(m, name))

        return o

    return func

def a_tree():
    return Tree('A', children=[
        Tree('B', []),
        Tree('BB', children=[
            Tree('C', []),
            Tree('CC', []),
            Tree('CCC', [])
        ]),
        Tree('BBB', []),
    ])

def a_aa_tree():
    return Tree('root', children=[
        Tree('A', children=[
            Tree('B', []),
            Tree('BB', children=[
                Tree('C', []),
                Tree('CC', []),
                Tree('CCC', [])
            ]),
            Tree('BBB', []),
        ]),
        Tree('AA', children=[
            Tree('B', []),
            Tree('BB', children=[
                Tree('C', []),
                Tree('CC', []),
                Tree('CCC', [])
            ]),
            Tree('BBB', []),
        ]),
    ])

@pytest.fixture(scope='session')
def get_a_tree():
    return a_tree()

@pytest.fixture(scope='session')
def get_a_aa_tree():
    return a_aa_tree()

@pytest.fixture(scope='session')
def get_a_aa_dict():
    return {
        'A': {
            'callback':     make_callback('A'),
            '-c':           {'help': 'A [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'A verbosity', 'action': 'store_true'},
        },
        'A|B': {
            'callback':     make_callback('A_B'),
            '-c':           {'help': 'A B [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'A B verbosity', 'action': 'store_true'},
        },
        'A|BB': {
            'callback':     make_callback('A_BB'),
            '-c':           {'help': 'A BB [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'A BB erbosity', 'action': 'store_true'},
            },
        'A|BB|C': {
            'callback':     make_callback('A_BB_C'),
            '-c':           {'help': 'A BB C [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'A BB C verbosity', 'action': 'store_true'},
        },
        'A|BB|CC': {
            'callback':     make_callback('A_BB_CC'),
            '-c':           {'help': 'A BB CC [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'A BB CC verbosity', 'action': 'store_true'},
        },
        'A|BB|CCC': {
            'callback':     make_callback('A_BB_CCC'),
            '-c':           {'help': 'A BB CCC [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'A BB CCC verbosity', 'action': 'store_true'},
        },
        'A|BBB': {
            'callback':     make_callback('A_BBB'),
            '-c':           {'help': 'A BBB [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'A BBB verbosity', 'action': 'store_true'},
        },
        'AA': {
            'callback':     make_callback('AA'),
            '-c':           {'help': 'AA [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'AA verbosity', 'action': 'store_true'},
        },
        'AA|B': {
            'callback':     make_callback('AA_B'),
            '-c':           {'help': 'AA B [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'AA B verbosity', 'action': 'store_true'},
        },
        'AA|BB': {
            'callback':     make_callback('AA_BB'),
            '-c':           {'help': 'AA BB [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'AA BB verbosity', 'action': 'store_true'},
            },
        'AA|BB|C': {
            'callback':     make_callback('AA_BB_C'),
            '-c':           {'help': 'AA BB C [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'AA BB C verbosity', 'action': 'store_true'},
        },
        'AA|BB|CC': {
            'callback':     make_callback('AA_BB_CC'),
            '-c':           {'help': 'AA BB CC [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'AA BB CC verbosity', 'action': 'store_true'},
        },
        'AA|BB|CCC': {
            'callback':     make_callback('AA_BB_CCC'),
            '-c':           {'help': 'AA BB CCC [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'AA BB CCC verbosity', 'action': 'store_true'},
        },
        'AA|BBB': {
            'callback':     make_callback('AA_BBB'),
            '-c':           {'help': 'AA BBB [optional pi]', 'action': 'store_const', 'const': 3.141593},
            '-v|--verbose': {'help': 'AA BBB verbosity', 'action': 'store_true'},
        },
    }

def create_table(args):
    return f'created table {args.name!r}'

def create_profile(args):
    return f'created profile {args.profile_name!r}'

def delete_table(args):
    return f'deleted table {args.table_name!r}'

def delete_profile(args):
    return f'deleted profile {args.name!r}'

def delete_profile_attribute(args):
    return f'updated profile {args.profile_name!r} by removing attribute {args.attribute_name!r}={args.attribute_value}'

def read_table(args):
    return f'read table {args.table_name!r}'

def update_table_name(args):
    return f'updated table from {args.old!r} to {args.new!r}'

def update_profile_add_attribute(args):
    return f'updated profile {args.profile_name!r} with attribute {args.attribute_name!r}={args.attribute_value}'

@pytest.fixture(scope='session')
def get_CRUD_dict():
    return {
        'create|table': {
            'callback': create_table,
            'name':     {'help': 'table name', 'action': 'store'},
        },
        'create|profile': {
            'callback': create_profile,
            'name':     {'help': 'table name', 'action': 'store'},
        },
        'delete|table': {
            'callback': delete_table,
            'name':     {'help': 'table name', 'action': 'store'},
        },
        'delete|profile': {
            'callback': update_profile_remove_attribute,
            'name':       {'help': 'profile name', 'action': 'store'},
        },
        'delete|profile|attribute': {
            'callback': update_profile_remove_attribute,
            'profile_name':   {'help': 'profile name', 'action': 'store'},
            'attribute_name': {'help': 'attribute name to add', 'action': 'store'},
            'attribute_value': {'help': 'attribute value', 'action': 'store'},
        },
        'read|table': {
            'callback': read_table,
            'name':     {'help': 'table name', 'action': 'store'},
            '-r|--rows':{'help': 'rows: [row_start, row_end]', 'nargs': 2, 'default': [None,None]},
            '-c|--cols':{'help': 'cols: [col_start, col_end]', 'nargs': 2, 'default': [None,None]},
        },
        'update|table|name': {
            'callback': update_table_name,
            'old':      {'help': 'old table name', 'action': 'store'},
            'new':      {'help': 'new table name', 'action': 'store'},
        },
        'update|profile|add|attribute': {
            'callback': update_profile_add_attribute,
            'profile_name':   {'help': 'profile name', 'action': 'store'},
            'attribute_name': {'help': 'attribute name to add', 'action': 'store'},
            'attribute_value': {'help': 'attribute value', 'action': 'store'},
        },
    }
