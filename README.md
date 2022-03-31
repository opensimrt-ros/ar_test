# ar_test

## Usage:

Catkin_make and source the catkin workspace with `ar_track_alvar`, `usb_cam` and this package at least. 

Then launch

    roslaunch ar_test usb_cal.launch

and

    roslaunch ar_test test.launch

You will need the cube with the fiducials as well, printed and assembled.

## Fix quaternions TF republisher:

To use run 

    ./fixquaternions.py

## Use dyn reconfigure:

First call the node `fixquaternions.py`. It is an executable, so you can just run it.

Then you have to use rqt like:

    rosrun rqt_gui rqt_gui -s reconfigure



## Calibrate:

If you are using a new webcame, then you need to run the opencv calibration:

    rosrun camera_calibration cameracalibrator.py --size 10x7 --square 0.025 image:=/usb_cam/image_raw camera:=/usb_cam

save the file and then load it into the launch file. you can copy how it was done in `usb_cal.launch` 
