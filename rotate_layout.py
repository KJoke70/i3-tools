#!/usr/bin/env python3

import i3ipc
import argparse

parser = argparse.ArgumentParser(description='rotate clockwise or counterclockwise')
parser.add_argument('direction', type=int, help='0 = clockwise, 1 = counterclockwise')
parser.add_argument('--times', '-t', type=int, default=1, help='how often to rotate')

args = parser.parse_args()

i3 = i3ipc.Connection()

root = i3.get_tree()
focused = root.find_focused()
leaves = focused.workspace().leaves()
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
        command += "[con_id=%s] focus;" % ( leaves[(old_focus - rotations) %
            number_of_leaves].id )
        i3.command(command)
elif args.direction == 1:
    if rotations > 0:
        for i in range(rotations):
            old_focus, new_comm = counterclock()
            command += new_comm
        command += "[con_id=%s] focus;" % ( leaves[(old_focus + rotations) %
            number_of_leaves].id )
        i3.command(command)
