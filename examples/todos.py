import model
from parsearg.parser import ParseArg
from parsearg.utils import (
    underline,
)


def main(args):
    args = args.split() if isinstance(args, str) else args
        
    d = {
        'purge|users': {
            'callback':   purge_users,
        },
        'purge|todos': {
            'callback':   purge_todos,
        },
        'create|user': {
            'callback':   create_user,
            'name':       {'help': 'create user name', 'action': 'store'},
            '-e|--email': {'help': "create user's email address", 'action': 'store', 'default': ''},
            '-p|--phone': {'help': "create user's phone number", 'action': 'store', 'default': ''},
        },
        'create|todo': {
            'callback':   create_todo,
            'user':       {'help': 'user name', 'action': 'store'},
            'title':      {'help': 'title of to-do', 'action': 'store'},
            '-c|--description': {'help': 'description of to-do', 'action': 'store', 'default': ''},
            '-d|--due-date': {'help': 'due date for the to-do', 'action': 'store', 'default': None},
        },
        'update|user|email': {
            'callback':   update_user_email,
            'name':       {'help': 'user name', 'action': 'store'},
            'email':      {'help': 'user email', 'action': 'store'},
        },
        'update|user|phone': {
            'callback':   update_user_phone,
            'name':       {'help': 'user name', 'action': 'store'},
            'phone':      {'help': 'user phone', 'action': 'store'},
        },
        'update|todo|title': {
            'callback':   update_todo_title,
            'id':         {'help': 'ID of to-do', 'action': 'store'},
            'title':      {'help': 'title of to-do', 'action': 'store'},
        },
        'update|todo|description': {
            'callback':   update_todo_description,
            'id':         {'help': 'ID of to-do', 'action': 'store'},
            'description':{'help': 'description of to-do', 'action': 'store'},
        },
    }
    parser = ParseArg(d=d, root_name='todos')

    # generate the argparse.Namespace by parsing the arguments:
    ns     = parser.parse_args(args)

    # perform the associated callback:
    result = ns.callback(ns)

    # display the result:
    print('{}\n\t{}\n'.format(underline(f'{args!r}'), result))


if __name__ == "__main__":
    args = sys.argv[1:] if len(sys.argv) > 1 else []

    EXIT_CODE = wrex(args)

    sys.exit(EXIT_CODE)
