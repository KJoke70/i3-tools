#!/usr/bin/env python3

import i3ipc
import argparse

parser = argparse.ArgumentParser(description='Check if program exists. \
                                 Focus if yes, otherwise start it.')
parser.add_argument('command', type=str, help='The command to run. The \
                    first word is expected to be the program name.')
parser.add_argument('--no-startup-id', '-nid', action='store_true',
        help='Use --no-startup-id')

args = parser.parse_args()
command = args.command
program = command.split()[0]
exec_command = "exec --no-startup-id " if args.no_startup_id else "exec "


def main():
    i3 = i3ipc.Connection()
    tree = i3.get_tree()
    ex = check_if_exists_and_focus(tree)
    if not ex:
        i3.on("window::new", on_window_new)
        i3.command(exec_command + command)
        try:
            i3.main()
        except:
            i3.main_quit()


def check_if_exists_and_focus(tree):
    classed = tree.find_classed("(?i)" + str(program))
    instanced = tree.find_instanced("(?i)" + str(program))
    if len(classed) > 0:
        classed[0].command("focus")
        return True
    elif len(instanced) > 0:
        instanced[0].command("focus")
        return True
    return False

def on_window_new(a, b):
    if check_if_exists_and_focus(a.get_tree()):
        a.main_quit()

if __name__ == '__main__':
    main()

