#!/usr/bin/env python3

import i3ipc
import argparse

parser = argparse.ArgumentParser(description='un-fullscreen current container, '
        'fullscreen next container, focus on new fullscreen')
parser.add_argument('direction', type=int, help='0: backwards, 1: forwards')
parser.add_argument('--times', '-t', type=int, default=1, help='how many '
        'times')
args = parser.parse_args()

i3 = i3ipc.Connection()

root = i3.get_tree()
focused = root.find_focused()
workspace = focused.workspace()
fullscreen = workspace.find_fullscreen()
leaves = workspace.leaves()
number_of_leaves = len(leaves)
times = args.times % number_of_leaves

def next(direction=1):
    command = ""
    old_index= -1
    for i in range(number_of_leaves):
        if leaves[i].id == fullscreen[0].id:
            old_index = i
    if old_index != -1:
        new_index = (old_index + direction) % number_of_leaves
    else:
        raise Exception("This shouldn't happen")
    return new_index

if(len(fullscreen) == 1 and number_of_leaves > 1 and times > 0):
    command = ""
    #command += "[con_id=%s] fullscreen toggle;" % (fullscreen[0].id)
    if args.direction == 0:
        for i in range(times):
            new_index = next(-1)
    elif args.direction == 1:
        for i in range(times):
            new_index = next(1)

    command += "[con_id=%s] fullscreen toggle;" % (leaves[new_index].id)
    command += "[con_id=%s] focus;" % (leaves[new_index].id)
    i3.command(command)


