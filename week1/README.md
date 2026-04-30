Week 1: ROS 2 Basics and Workspace Setup
This lab focused on setting up a ROS 2 development environment, creating a workspace, and building my first ROS 2 package with a simple Python node. 
The main objective was to understand fundamental ROS 2 concepts including nodes, packages, workspaces, and the build process.
By the end of this lab, the following were successfully created:
1. Created a ROS2 workspace
2. Built the workspace using Colcon build
3. Created a python package
4. Implemented and registered a node
5. Exceuted the node using ros2 run

Commands Used:
1. ROS 2 Verification:
source /opt/ros/humble/setup.bash
lsb_release -a

2. Create Workspace:
mkdir -p ~/ros2_ws_rafay/src
cd ~/ros2_ws_rafay
colcon build
source install/setup.bash

3. Create Package:
cd ~/ros2_ws_rafay/src
ros2 pkg create --build-type ament_python my_first_pkg
cd ~/ros2_ws_rafay
colcon build
source install/setup.bash
ros2 pkg list | grep my_first_pkg

4. Create Node File:
cd ~/ros2_ws_rafay/src/my_first_pkg/my_first_pkg/
nano simple_node.py
chmod +x simple_node.py

5. Register Entry Point:
cd ~/ros2_ws_rafay/src/my_first_pkg/
nano setup.py

6. Build and Run:
cd ~/ros2_ws_rafay
colcon build
source install/setup.bash
ros2 run my_first_pkg simple_node

Problems Faced and Solutions:
Problem 1: ROS 2 commands not found
Issue: When opening a new terminal, ros2 commands would not work.
Solution: Added sourcing to .bashrc file to automatically source ROS 2 in every new terminal.

Problem 2: Package not found after build
Issue: Running ros2 pkg list | grep my_first_pkg showed no results.
Solution: Forgot to source the workspace after building. Ran source install/setup.bash to fix.

Problem 3: "Executable not found" error
Issue: When running ros2 run my_first_pkg simple_node, got error that executable doesn't exist.
Solution: Realized I forgot to add the entry point in setup.py. Added the console_scripts configuration and rebuilt.

Problem 4: Permission denied
Issue: Couldn't run the Python script directly.
Solution: Used chmod +x to make the file executable.

Reflection:
This lab helped me understand the foundational workflow of ROS 2 development. I learned how important environment sourcing is and how the workspace structure organizes packages and build outputs. 
Creating and registering a Python node clarified how ROS 2 executes code through entry points. I also developed confidence using Linux terminal commands. 
Troubleshooting errors improved my understanding of build systems and environment variables. Overall, this lab established a strong base for future robotics development tasks.
