# i3-tools
Small scripts to extend the [i3wm](https://i3wm.org/) window manager. For requirements see `Pipfile` and `Pipfile.lock`.

## rotate_layout.py ##
A script to rotate the current layout clockwise or counterclockwise. This
script also supports multiple monitors. This can also be turned off (see
usage).
#### Dependencies ####

 * [i3ipc](https://github.com/acrisci/i3ipc-python) : `pip install --user i3ipc`

#### Usage ####
`rotate_layout.py [-h] [--times N] direction`

 * direction:
   * 0 : clockwise
   * 1 : counterclockwise
 * -h : help
 * --times/-t N: rotate N times
 * --no-multimonitor/-m: disables multimonitor support

#### Examples ####

![rotate_layout example 1](images/01_rotate_layout.gif)

![rotate_layout example 2](images/02_rotate_layout.gif)

![rotate_layout example 3](images/04_rotate_layout.gif)

#### Note ####

* Performance might be slow with a lot of containers.
* The [i3wm User's Guid](https://i3wm.org/docs/userguide.html#_swapping_containers) states:
     > Note that swapping does not work with all containers. Most notably, swapping floating containers or containers that have a parent-child relationship to one another does not work.
     so this script might not work for every layout.
* The script doesn't know how your monitors are set up so things might get
    confusing if you use more than 2 displays.

## fullscreen_mode.py ##
A script to switch to different containers in fullscreen mode. This can also be done with `rotate_layout.py` but is significantly faster because no containers are swapped around (and the layout stays as is).

#### Dependencies ####

 * [i3ipc](https://github.com/acrisci/i3ipc-python) : `pip install --user i3ipc`

#### Usage ####
`fullscreen_mode.py [-h] [--times N] direction`

 * direction:
   * 0 : backwards
   * 1 : forwards
 * -h : help
 * --times/-t N: move N times forwards/backwards

#### Examples ####

![fullscreen_mode example 1](images/01_fullscreen_mode.gif)
