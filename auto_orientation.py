#!/usr/bin/env python3
# idea: https://www.reddit.com/r/i3wm/comments/8zjixh/automatic_split_direction/

import i3ipc

i3 = i3ipc.Connection()

def on_window_focus(change, container):
    focused = i3.get_tree().find_focused()
    if focused.type == "con":
        width = focused.rect.width
        height = focused.rect.height
        if width > height:
            focused.command('split horizontal')
        else:
            focused.command('split vertical')

try:
    i3.on('window::focus', on_window_focus)
    i3.main()
finally:
    i3.main_quit()



