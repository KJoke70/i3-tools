#!/usr/bin/env python3

import i3ipc
import argparse

parser = argparse.ArgumentParser(description='focus on sibling in' \
        'next/prev top-level container')
parser.add_argument('direction', help='left=-1, right=1', \
        type=int)

args = parser.parse_args()

direction = args.direction

i3 = i3ipc.Connection()
con = i3.get_tree().find_focused()

# find outermost parent
counter = 0 # how often to ascend to outermost parent
while con.parent.type != "workspace":
    con = con.parent
    counter += 1

nodes = con.parent.nodes
index = 0

# find left/right sibling of outermost parent
for l in nodes:
    if l.id == con.id:
        break
    index += 1
index += direction
if index >= len(nodes) or index < 0:
    exit()

# descent to level 'counter' or a lowest leaf
con2 = nodes[index]
for i in range(counter, 0, -1):
    n = con2.nodes
    if len(n) == 0:
        break #exit()?
    else:
        con2 = n[direction]

con2.command('focus')
