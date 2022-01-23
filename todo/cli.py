import argparse
from todo.data_manager import add_list, add_task, remove_task, remove_list, edit_task, rename_list, list_info
parser = argparse.ArgumentParser(description='simple to-do list')
subparser = parser.add_subparsers(dest='command')

# commands
add = subparser.add_parser('add', help='add a new task or list')
rm = subparser.add_parser('rm', help='remove tasks or lists')
edit = subparser.add_parser('edit', help='edit task/list details')
check = subparser.add_parser('check', help='mark task as completed')
uncheck = subparser.add_parser('uncheck', help='mark task as not completed')
ls = subparser.add_parser('ls', help='list all tasks in a list')
show = subparser.add_parser('show', help='displays task details')


# add
def parse_add(args):
    if not args.TASKS:
        add_list(args.LIST)
    else:
        deadline = args.deadline if args.deadline else None
        priority = args.priority if args.priority else 0
        notes = args.notes if args.notes else None
        for task in args.TASKS:
            add_task(task, args.LIST, deadline, priority, notes)


add.add_argument('LIST', type=str)
add.add_argument('TASKS', type=str, nargs='*')
add.add_argument('--deadline', type=str)
add.add_argument('--priority', type=int)
add.add_argument('--notes', type=str)
add.set_defaults(func=parse_add)


# rm
def parse_rm(args):
    if not args.TASKS:
        remove_list(args.LIST)
    else:
        for task in args.TASKS:
            remove_task(task, args.LIST)


rm.add_argument('LIST', type=str)
rm.add_argument('TASKS', type=str, nargs='*')
rm.set_defaults(func=parse_rm)


# edit
def parse_edit(args):
    if not args.TASKS:
        rename_list(args.LIST, args.name)
    else:
        changes = {arg: args[arg] for arg in ['name', 'list', 'deadline', 'priority', 'notes'] if arg}
        for task in args.TASKS:
            edit_task(task, args.LIST, changes)


edit.add_argument('LIST', type=str)
edit.add_argument('TASKS', type=str, nargs='*')
edit.add_argument('--name', type=str)
edit.add_argument('--list', type=str)
edit.add_argument('--deadline', type=str)
edit.add_argument('--priority', type=int)
edit.add_argument('--notes', type=str)
edit.set_defaults(func=parse_edit)


# check
def parse_check(args):
    for task in args.TASKS:
        edit_task(task, args.LIST, {'done': True})


check.add_argument('LIST', type=str)
check.add_argument('TASKS', type=str, nargs='+')
check.set_defaults(func=parse_check)


# uncheck
def parse_uncheck(args):
    for task in args.TASKS:
        edit_task(task, args.LIST, {'done': False})


uncheck.add_argument('LIST', type=str)
uncheck.add_argument('TASKS', type=str, nargs='+')
uncheck.set_defaults(func=parse_uncheck)


# ls
def parse_ls(args):
    if not args.LIST:
        # display functon?
        raise 'Not implemented'
    else:
        list_info(args.LIST[0])


ls.add_argument('LIST', type=str, nargs='*')
ls.set_defaults(func=parse_ls)

# show
show.add_argument('LIST', type=str)
show.add_argument('TASK', type=str)
show.set_defaults(func=show)

args = parser.parse_args()
print(args)
args.func(args)