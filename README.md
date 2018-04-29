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

## fullscreen_mode.py ##
A script to switch to different containers in fullscreen mode. This can also be done with `rotate_layout.py` but is significantly faster because no containers are swapped around (and the layout stays as is).

#### Dependencies ####

 * [i3ipc](https://github.com/acrisci/i3ipc-python) : `pip install --user i3ipc`

#### Usage ####
`rotate_layout.py [-h] [--times N] direction`

 * direction:
   * 0 : backwards
   * 1 : forwards
 * -h : help
 * --times/-t N: move N times forwards/backwards

#### Examples ####

![fullscreen_mode example 1](images/01_fullscreen_mode.gif)
