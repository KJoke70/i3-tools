#!/usr/bin/env python3

import i3ipc
import subprocess


i3 = i3ipc.Connection()

windows = i3.get_tree().scratchpad().leaves()

d = dict()

for w in windows:
    d["[%s] %s" % (w.window_class, w.name)] = w.id

keys = [x for x in d.keys()]

s = ""
for x in d.keys():
    s += x + "\n"


try:
    ps = subprocess.Popen(("echo", s), stdout=subprocess.PIPE)
    output = subprocess.check_output(("dmenu","-p", "Scratchpad:", "-l", "10"), stdin=ps.stdout)
    ps.wait()

    key = output.decode('utf-8').rstrip()
    value = d[key]

    i3.command("[con_id='%s'] scratchpad show; move position center; floating toggle" % value)
except:
    pass


