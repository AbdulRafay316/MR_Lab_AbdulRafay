Node: A node is a computational process in ROS 2 that performs specific tasks such as controlling a motor or processing sensor data.
Topic: A topic is a named communication bus over which nodes exchange messages asynchronously using a publish-subscribe pattern.
Package: A package is the fundamental unit of ROS 2 software organization containing code, dependencies, and build information.
Workspace: A workspace is a directory structure where ROS 2 packages are developed, built, and installed.

2. Explain why sourcing is required. What happens if you do not source a workspace?
Sourcing is required because it adds the workspace's setup.bash file to the current shell session, making ROS 2 commands available and allowing the system to locate installed packages. 
If you do not source a workspace, the terminal will not recognize ROS 2 commands (resulting in "command not found" errors) and cannot find packages you've built in that workspace.

3. What is the purpose of colcon build? What folders does it generate?
The purpose of `colcon build` is to compile and build all packages in the workspace, making them ready for execution. It generates four folders:
- build/  Contains intermediate build files and compilation artifacts
- install/  Contains the installed packages and setup files for sourcing
- log/  Stores build logs and error messages for debugging
- src/  (pre-existing) Contains the source code of your packages

4. In your own words, explain what the entry_points console script does in setup.py.
The entry_points console_scripts section in setup.py acts as a registry that maps executable names to specific Python functions. 
When I type `ros2 run my_first_pkg simple_node`, ROS 2 looks up this mapping in setup.py to find which Python function to execute, allowing my Python script to become a runnable ROS 2 node.

5. Draw (by hand or ASCII) a diagram showing one publisher and one subscriber connected by a topic.
                PUBLISHER-SUBSCRIBER DIAGRAM
                
+----------------+                          +----------------+
|                |                          |                |
|   PUBLISHER    |                          |  SUBSCRIBER    |
|                |                          |                |
|   /talker      |                          |   /listener    |
|                |                          |                |
+-------+--------+                          +-------+--------+
        |                                           ^
        | Publishes                                 |
        | to topic                                  | Subscribes
        |                                           | to topic
        v                                           |
    +-------------------------------------------------+
    |                                                 |
    |                    TOPIC                        |
    |                  "/chatter"                     |
    |                                                 |
    +-------------------------------------------------+
