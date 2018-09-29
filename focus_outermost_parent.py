#!/usr/bin/env python3

import i3ipc

i3 = i3ipc.Connection()
con = i3.get_tree().find_focused()
while con.parent.type != "workspace":
    con = con.parent

con.command('focus')
