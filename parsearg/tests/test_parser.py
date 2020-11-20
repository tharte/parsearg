import pytest
import argparse
from parsearg.parser import (
    ParseArg,
)
from parsearg.utils import (
    underline,
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

d = {
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


def test_ParseArg():
    # create the parse from the dict (flat tree)
    parser = ParseArg(d, root_name='root')

    def do_it(node):
        def _do_it(args):
            # generate the argparse.Namespace by parsing the arguments:
            ns     = parser.parse_args(args)

            # perform the associated callback:
            result = ns.callback(ns)

            # display the result:
            print('{}\n{}'.format(underline(f'{args!r}'), result))

        print(underline(f'\n\nNODE :: {node!r}'))
        with pytest.raises(SystemExit):
            _do_it(f'{node} -h')
        print('\n')

        _do_it(f'{node}')
        _do_it(f'{node} -v')
        _do_it(f'{node} -c')
        _do_it(f'{node} -v -c')

    nodes = [
        'A',
        'A B',
        'A BB',
        'A BB C',
        'A BB CC',
        'A BB CCC',
        'AA',
        'AA B',
        'AA BB',
        'AA BB C',
        'AA BB CC',
        'AA BB CCC',
    ]
    list(map(lambda node: do_it(node), nodes))

