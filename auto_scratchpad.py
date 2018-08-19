#!/usr/bin/env python3

import argparse
import i3ipc

def workspace_args(s):
    """
    argparse type to accept arguments separated by comma.
    floating,name,class_name,instance,role,mark
    """
    try:
        floating, name, class_name, instance, role, mark   = map(str, s.split(','))
        return floating == 'True', name, class_name, instance, role, mark
    except:
        raise argparse.ArgumentTypeError('Criteria must be ' \
                'floating,name,class_name,instance,role,mark')

# command line arguments
parser = argparse.ArgumentParser(description='Move a container matching ' \
        'cirteria to scratchpad upon focus change')
parser.add_argument('criteria', help='criteria for which containers to hide ' \
        'floating,name,class_name,instance,role,mark ...', \
        type=workspace_args, nargs='+')

args = parser.parse_args()
floating, names, classes, instances, roles, marks = zip(*args.criteria)

i3 = i3ipc.Connection()
last_matched = None

def check_condition(container):
    """
    check if the container matches the specified criteria
    """
    w_name = container.name
    w_class = container.window_class
    w_instance = container.window_instance
    w_role = container.window_role
    w_marks = container.marks
    w_fullscreen = container.fullscreen_mode # 1 if window in fullscreen (1)
    w_urgent = container.urgent
    w_floating = container.floating

    for i in range(len(args.criteria)):
        if (floating[i] == ('on' in w_floating)) and \
                (names[i] == '' or names[i] == w_name) and \
                (classes[i] == '' or classes[i] == w_class) and \
                (instances[i] == '' or instances[i] == w_instance) and \
                (roles[i] == '' or roles[i] == w_role) and \
                (marks[i] == '' or marks[i] in w_marks):
            return True
    return False


def move_to_scratchpad(w_id):
    """ try to move window with con_id=w_id to scratchpad """
    i3.command('[con_id=%s] move scratchpad' % (str(w_id)))

def on_window_focus(self, e):
    """
    on focus event:
        * check if focus is different from the last matched window. Move to
          scratchpad if yes
        * check if current window matches criteria and set as last_matched if
          yes
    """

    global last_matched
    w_id = e.container.id

    if w_id != last_matched:
        move_to_scratchpad(last_matched)
        last_matched = None

    if check_condition(e.container):
        last_matched = w_id


# listen to focus event
try:
    i3.on('window::focus', on_window_focus)
    i3.main()
finally:
    i3.main_quit()
