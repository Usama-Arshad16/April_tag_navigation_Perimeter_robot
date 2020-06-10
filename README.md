# April_tag_navigation_Perimeter_robot

Installation Method:

Open the "perimeter_robot/agriculture_world/models" folder inside the package.

Copy all the items.

Go to the "home" directory.

Show the hidden files.

Then open the ".gazebo/models".

Paste the items.

Place the "warehouse_world" package at "catkin_ws/src"

open the terminal and use the commands below.

$ cd ~/catkin_ws

$ catkin_make

$ source devel/setup.bash

Simulation:

Open 4 terminals and use these 4 commands. Only One in each terminal

$ roslaunch perimeter perimeter.launch

$ roslaunch perimeter move_base.launch

$ roslaunch perimeter view_robot.launch

$ rosrun perimeter_control navigate.py
