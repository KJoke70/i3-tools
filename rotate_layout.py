#!/usr/bin/env python3

import i3ipc
import argparse

parser = argparse.ArgumentParser(
                    description='rotate clockwise or counterclockwise.')
parser.add_argument('direction', type=int,
                    help='0 = clockwise, 1 = counterclockwise.')
parser.add_argument('--times', '-t', type=int, default=1,
                    help='how often to rotate.')
parser.add_argument('--no-multimonitor', '-m', action='store_true',
        help='disables multi-monitor support.')
parser.add_argument('--enable-floating', '-f', action='store_true',
        help='explicitly allow floating windows. May behave unexpectedly.')

args = parser.parse_args()


i3 = i3ipc.Connection()

#check if multiple displays attached
active_displays = 0
active_workspaces = list()
for d in i3.get_outputs():
    if d.active:
        active_displays += 1
        active_workspaces.append(int(d.current_workspace))

root = i3.get_tree()
focused = root.find_focused()

if args.no_multimonitor or active_displays == 1:
    leaves = focused.workspace().leaves()

else:
    focused_num = focused.workspace().num
    f_ind = active_workspaces.index(focused_num)
    active_workspaces[0], active_workspaces[f_ind] = active_workspaces[f_ind], active_workspaces[0]

    w_spaces = root.workspaces()

    leaves = list()
    for ws in root.workspaces():
        if ws.num in active_workspaces:
            if ws.num == focused_num:
                leaves = ws.leaves() + leaves
            else:
                leaves += ws.leaves()

if not args.enable_floating:
    to_remove = list()
    for i in range(len(leaves)):
        if 'on' in leaves[i].floating:
            to_remove.append(i)
    for i in range(len(to_remove)-1, -1, -1):
        del leaves[to_remove[i]]


number_of_leaves = len(leaves)
rotations = args.times % number_of_leaves

def clock():
    old_focus = number_of_leaves - 1
    comm = ""
    for i in range(number_of_leaves-1):
        if leaves[i].id == focused.id:
            old_focus = i
        comm += '[con_id=%s] swap container with con_id %s;' % (str(leaves[i].id),
            str(leaves[i+1].id))
    return old_focus, comm

def counterclock():
    old_focus = 0
    comm = ""
    for i in range(number_of_leaves-1, 0, -1):
        if leaves[i].id == focused.id:
            old_focus = i
        if i > 0:
            comm += '[con_id=%s] swap container with con_id %s;' % (str(leaves[i].id),
                str(leaves[i-1].id))
    return old_focus, comm

command = ""
if args.direction == 0:
    if rotations > 0:
        for i in range(rotations):
            old_focus, new_comm = clock()
            command += new_comm
        if not args.enable_floating and 'on' in focused.floating:
            command += "[con_id=%s] focus;" % ( focused.id )
        else:
            command += "[con_id=%s] focus;" % ( leaves[(old_focus - rotations) %
                number_of_leaves].id )
        i3.command(command)
elif args.direction == 1:
    if rotations > 0:
        for i in range(rotations):
            old_focus, new_comm = counterclock()
            command += new_comm
        if not args.enable_floating and 'on' in focused.floating:
            command += "[con_id=%s] focus;" % ( focused.id )
        else:
            command += "[con_id=%s] focus;" % ( leaves[(old_focus + rotations) %
                number_of_leaves].id )
        i3.command(command)
