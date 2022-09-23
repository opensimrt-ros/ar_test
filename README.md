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

If you are using an uncalibrated camera, such as new webcam, then you need to run the opencv calibration. You can print a calibration checkerboard pattern from [here](https://markhedleyjones.com/projects/calibration-checkerboard-collection). I got the 11x8 squares (which camera calibrator calls 10x7 because it refers to the number of vertices). If you print a different one, you will need to change the options below.

This will take a while as the algorithm needs to take a bunch of different pictures of the checkerboard pattern in different distances and orientations.

The run:

    rosrun camera_calibration cameracalibrator.py --size 10x7 --square 0.025 image:=/usb_cam/image_raw camera:=/usb_cam

save the file and then load it into the launch file. you can copy how it was done in `usb_cal.launch` 
