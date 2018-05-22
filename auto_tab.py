#!/usr/bin/env python3

import i3ipc
import argparse



def workspace_args(s):
    """ argparse type to accept two arguments separated by comma """
    try:
        class_name, layout = map(str, s.split(','))
        if layout != "stacking" and layout != "tabbed":
            raise
        return class_name, layout
    except:
        raise argparse.ArgumentTypeError('class/layout must be ' \
                'class_name,layout. Layout must be either stacking or tabbed')


parser = argparse.ArgumentParser(description='automatically ' \
        'stack/tab windows of a class')
parser.add_argument('class_layout', help='define class_name and layout like ' \
        ' class_name1,layout1 class_name2,layout2 ...', \
        type=workspace_args, nargs='+')

args = parser.parse_args()

# variables
class_names, layouts = zip(*args.class_layout)
container_info = dict()
for c in class_names:
    container_info[c] = dict()



def instance_index_on_ws(c, ws, w_id):
    """ notes down the new instance and returns the index """
    if ws in container_info[c].keys():
        container_info[c][ws][w_id] = False
        return len(container_info[c][ws]) - 1
    else:
        container_info[c][ws] = dict()
        container_info[c][ws][w_id] = True
        return 0

def close_window(c, w_id):
    """ remove w_id from database """
    for ws in container_info[c].keys():
        if w_id in container_info[c][ws]:
            del container_info[c][ws][w_id]


def get_data(i3, e):
    w_id = e.container.id
    w_layout = e.container.layout
    w_num = None

    tree = i3.get_tree()
    for w in tree.workspaces():
        if w.find_by_id(w_id) != None:
            w_num = w.num
    return w_id, w_num, w_layout


def on_new_window(i3, e):
    w_class = e.container.window_class
    if w_class in class_names:
        w_id, w_num, w_layout = get_data(i3, e)
        w_ind = instance_index_on_ws(w_class, w_num, w_id)
        #print(w_id, w_num, w_layout, w_ind)


def on_window_close(i3, e):
    w_class = e.container.window_class
    if w_class in class_names:
        w_id, w_num, w_layout = get_data(i3, e)
        close_window(w_class, w_id)






i3 = i3ipc.Connection()
i3.on('window::new', on_new_window)
i3.on('window::close', on_window_close)
i3.main()
