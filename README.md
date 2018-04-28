# i3-tools
Small scripts to extend the [i3wm](https://i3wm.org/) window manager. For requirements see `Pipfile` and `Pipfile.lock`.

## rotate_layout.py ##
A script to rotate the current layout clockwise or counterclockwise.
#### Dependencies ####

 * [i3ipc](https://github.com/acrisci/i3ipc-python) : `pip install --user i3ipc`

#### Usage ####
`rotate_layout.py [-h] [--times N] direction`

 * direction:
   * 0 : clockwise
   * 1 : counterclockwise
 * -h : help
 * --times/-t N: rotate N times

#### Examples ####

![rotate_layout example 1](images/01_rotate_layout.gif)

![rotate_layout example 1](images/02_rotate_layout.gif)

