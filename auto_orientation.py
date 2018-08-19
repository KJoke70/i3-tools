#!/usr/bin/env python3
# idea: https://www.reddit.com/r/i3wm/comments/8zjixh/automatic_split_direction/

import i3ipc

i3 = i3ipc.Connection()

def on_window_focus(_, props):
    tree = i3.get_tree()
    focused = tree.find_focused()

    #print(props.container.id)
    parent_id = focused.parent.id
    parent = tree.find_by_id(id)
    print(parent_id, focused.id)
    print(dir(parent))
    print(tree.layout)
    print(tree.orientation)
    print(dir(focused.leaves))
    print(focused.parent.leaves()[0])

    if focused.type == "con":
        width = focused.rect.width
        height = focused.rect.height
        if width > height:
            focused.command('split horizontal')
        else:
            focused.command('split vertical')
#    print(dir(focused))
#    print(focused.orientation)
#    print(focused.layout)
#    print(dir(focused.props.change]))
#    print(dir(focused.parent))
#    print(focused.props.layout)
    #print(props.container.orientation)
    #print(props.container.layout)
    #print(dir(props.container.props))
    #print(dir(props.container.parent))
    print()

try:
    i3.on('window::focus', on_window_focus)
    i3.main()
finally:
    i3.main_quit()



