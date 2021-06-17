# oryksbot - A differential Drive Robot Kit for learning ROS

![oryksbot assembly](https://github.com/lyleokoth/oryksbot/blob/main/resources/diff_1.JPG?raw=true)

This repository contains all the files and code needed to simulate the oryksbot, a differential robot, using [Gazebo](http://gazebosim.org/)  and [ROS](https://www.ros.org/).
The software runs on [ROS noetic](http://wiki.ros.org/noetic) and [Ubuntu 20.04](http://www.releases.ubuntu.com/20.04/). If you want to use a different ROS version, you might have to do some changes to the source code.
The repo also contains the firmware needed to set up the robot, i.e the motor controllers, the lidar sensor
readers as well as the code for reading other sensors such as the IMU.

## The Motivation

The aim was to come up with an affordable robotics kit for learning mobile robotics using [The Robot Operating System(ROS)](https://www.ros.org/). Initially this simulation uses turtlebot3 burger, but the CAD files for oryksbot will be availed soon. The design of oryks bot was mainly influenced by the pricing and ease of assembly. As such, the parts are either easily 3d printed and drilled for connections or available off-the-shelf. The available robotics kits are either too expensive or just costly to import in some parts of the world such as Kenya.

![oryksbot parts list](https://github.com/lyleokoth/oryksbot/blob/main/resources/diff_2.JPG?raw=true)

## The electronics components used are easily available:
 - Raspberry Pi A3+
 - Arduino Nano
 - RPLidar
 - Raspberry Pi Camera
 - Motor Controller
 - Voltage Regulator
 - Lipo battery
 - The Motor Pair

![oryksbot electronics](https://github.com/lyleokoth/oryksbot/blob/main/resources/diff_6.JPG?raw=true)

To get started, ensure you are running a computer with [Ubuntu 20.04 Focal Fossa](http://www.releases.ubuntu.com/20.04/) and ROS noetic installed. Folow the instruction on [ROS installation](http://wiki.ros.org/noetic) if not.

## Setup
```
git clone https://github.com/lyleokoth/oryksbot.git
cd oryksbot
catkin_make
source devel/setup.bash
```

## Run
```
source devel/setup.bash
roslaunch oryksbot_gazebo oryksbot_gazebo.launch
```
After all the nodes have started, you can start using your joystick to control the robot.
Driving forward or backwards is achieved using the left joystick axis by moving it up and down. Turning sideways is achieved by moving the right joystick axis left to right or vice versa.

## The Project Workspace

The project workspace consists of four main packages:
- oryksbot_description
- oryksbot_gazebo
- oryksbot_control
- oryksbot_mapping
- oryksbot_navigation

## TO DO

Describe the packages; show their uses
 
