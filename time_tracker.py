#!/usr/bin/env python3

#import sys
import os
import time
#import argparse
import configparser
import i3ipc

#import csv
import json

import socket #ipc
import threading
import subprocess

total_time = 0
current_time = 0

## Needs to track
##  window::focus
##  window::new
##  window::close
##  window::title

# TODO check focus bug with floating

def main():
    # 1. arguments:
    #   - path to config
    # 2. check backup_dir for file of same day
    #   - load backup, if from same day
    #   - otherwise, start anew
    # 3. create notification threads to notify upon time x (specified in config)
    #   - class, instance, name, role, mark have reached time x
    #   - take break, drink, etc (config)
    #       + every x min (when active for x, TODO DPMS ??), only start next
    #           round, after notification was clicked
    #       + specific times
    # 4. count time for currently focused
    # 5. stop counting once focus changes -> change count
    # 6. save count in dictionary
    # 7. backup save every 5 minutes (or set in config)
    # 8. send info to IPC calls # TODO how??
    #
    try:
        i3 = i3ipc.Connction()
        i3.on("window::focus", on_window_focus)
        i3.on("window::new", on_window_new)
        i3.on("window::title", on_window_title)
        i3.on("window::close", on_window_close)
        i3.main()
    except Exception as e:
        print(e)
    finally:
        i3.main_quit()
        # save to file (race condition ?)


















def on_window_focus(a, b):
    pass

def on_window_new(a, b):
    pass

def on_window_close(a, b):
    pass

def on_window_title(a, b):
    pass




def backup_data(data, path):
    """ backup data to path. Is meant to be called periodically. """
    pass # TODO

def load_backup(path):
    """ load data from backup path. Compares if file is from the same day. If
    not, returns empty data. """
    pass # TODO





if __name__ == "__main__":
    main()
