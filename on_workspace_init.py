#!/usr/bin/env python3

import argparse
import i3ipc

def workspace_args(s):
    """ argparse type to accept two arguments separated by comma """
    try:
        ws, cmd = map(str, s.split(','))
        return ws, cmd
    except:
        raise argparse.ArgumentTypeError('Workspaces/commands must be ws,cmd')

parser = argparse.ArgumentParser(description='Execute a command upon ' \
        'creation of a workspace.')
parser.add_argument('ws_cmd', help='define workspaces and commnands like ' \
        ' ws1,cmd1 ws2,cmd2,...', type=workspace_args, nargs='+')
parser.add_argument('--no-exec', '-n', action='store_true', \
        help='Disables automatic exec before command. Requires you to ' \
        'write every command fully, e.g exec firefox. Also allows the usage ' \
        'of i3 commands')

args = parser.parse_args()
workspaces, commands = zip(*args.ws_cmd)

def on_workspace_init(self, e):
    """ execute command if a specific workspace was created """
    if e.current and e.current.name in workspaces:
        index = workspaces.index(e.current.name)
        if args.no_exec:
            i3.command('%s' % (commands[index]))
        else:
            i3.command('exec %s' % (commands[index]))

i3 = i3ipc.Connection()
i3.on('workspace::init', on_workspace_init)
i3.main()
