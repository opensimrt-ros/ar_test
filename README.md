# ar_test

## Usage:

Catkin_make and source the catkin workspace with `ar_track_alvar`, `usb_cam` and this package at least. 

Then launch

    roslaunch ar_test usb_cal.launch

and

    roslaunch ar_test test.launch

You will need the cube with the fiducials as well, printed and assembled. The file is ar_cube.png, courtesy of [Ishijima Electronics](http://ishi.main.jp/ros/ros_ar_bundle.html).

## Fix quaternions TF republisher:

To use run 

    ./fixquaternions.py

## Use dyn reconfigure:

First call the node `fixquaternions.py`. It is an executable, so you can just run it.

Then you have to use rqt like:

    rosrun rqt_gui rqt_gui -s reconfigure



## Calibrate:

If you are using a new webcam, then you need to run the opencv calibration:

    rosrun camera_calibration cameracalibrator.py --size 10x7 --square 0.025 image:=/usb_cam/image_raw camera:=/usb_cam

save the file and then load it into the launch file. you can copy how it was done in `usb_cal.launch` 

## fixquaternions2.py

use this to republish the exact same quaternion, because we fixed it in the SimpleServer when we are stacking the quaternion components

- z -> +y
- x -> +z
- y -> +x

this was a simple transformation to fix. now the paper cube, if you turn the algorithm on while it is pointed towards the screen like:

- Z pointing towards screen (x)
- Y pointing towards right ->
- X pointing up A

Then it aligns when used with OpenSimRT branch ros\_fixing\_cube v0.02.1

# TODO:

- fixquaternions should be parametrized
- create launch files for fixquaternions*
- 
