import pytest
from parsearg.parser import (
    ParseArg,
)
from parsearg.utils import (
    underline,
)

def test_ParseArg(get_a_aa_dict):
    # create the parser from the dict (flat tree)
    parser = ParseArg(d=get_a_aa_dict, root_name='root')

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


def test_CRUD(get_CRUD_dict):
    # create the parse from the dict (flat tree)
    parser = ParseArg(d=get_CRUD_dict, root_name='CRUD')

    def do_it(args):
        # generate the argparse.Namespace by parsing the arguments:
        ns     = parser.parse_args(args)

        # perform the associated callback:
        result = ns.callback(ns)

        # display the result:
        print('{}\n\t{}\n'.format(underline(f'{args!r}'), result))

    nodes = [
        'create table -n tab',
        'create profile -n tharte',
        'read table -n tab',
        'update table name',
        'purge Todo',                   # purge Todo table
        'purge User',                   # purge User table
        'purge all',                    # purge all tables
    ]

    nodes = [
        'purge User',                   # purge all records from the User table
        'purge Todo',                   # purge all records from the Todo table
        'create user foo foo@foo.com',
        'create user bar bar@bar.com',
        'create user qux qux@qux.com',
        'create todo foo title1 description1 2020-11-30',
        'create todo foo title2 description2 2020-12-31',
        # 'update todo title id title',
        # 'update todo description id description',
    ]

    list(map(lambda node: do_it(node), nodes))
