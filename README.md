# oryksbot - A differential Drive Robot Kit for learning ROS

![oryksbot assembly](https://github.com/lyleokoth/oryksbot/blob/main/resources/diff_1.JPG?raw=true)

This repository contains all the files and code needed to simulate the oryksbot, a differential robot, using [Gazebo](http://gazebosim.org/)  and [ROS](https://www.ros.org/).
The software runs on [ROS noetic](http://wiki.ros.org/noetic) and [Ubuntu 20.04](http://www.releases.ubuntu.com/20.04/). If you want to use a different ROS version, you might have to do some changes to the source code.
The repo also contains the firmware needed to set up the robot, i.e the motor controllers, the lidar sensor
readers as well as the code for reading other sensors such as the IMU.

The aim was to come up with an affordable robotics kit for learning mobile robotics using [The Robot Operating System(ROS)](https://www.ros.org/). Initially this simulation uses turtlebot3 burger, but the CAD files for oryksbot will be availed soon. The design of oryks bot was mainly influenced by the pricing and ease of assembly. As such, the parts are either easily 3d printed and drilled for connections or available off-the-shelf. 

![oryksbot parts list](https://github.com/lyleokoth/oryksbot/blob/main/resources/diff_2.JPG?raw=true)
 
