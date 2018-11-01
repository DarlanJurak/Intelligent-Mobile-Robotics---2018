# ROS PACKAGE - Creation, compilation and execution

## 1. Create pkg in the **current directory** (do it on src/):

    # roscreate-pkg [pkg_name] [depend1] [depend2] [depend3] [depend4]
    $ roscreate-pkg beginner_tutorials std_msgs rospy roscpp

## 2. Build pkg:

    # rosmake [pkg]
    $ rosmake beginner_tutorials

## 3. Write and save main files:
    
    # files from: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29
    # listener: https://raw.githubusercontent.com/ros/ros_tutorials/kinetic-devel/roscpp_tutorials/listener/listener.cpp
    # talker: https://raw.githubusercontent.com/ros/ros_tutorials/kinetic-devel/roscpp_tutorials/talker/talker.cpp

    # Add files (.cpp or .py) on ".../pkg/src"

## 4. Edit file "CMakeLists.txt":

    # rosed beginner_tutorials CMakeLists.txt
    $ rosed [pkg] CMakelists.txt

### 4.1 Add the following lines (listener/talker specific):

    rosbuild_add_executable(talker src/talker.cpp)
    rosbuild_add_executable(listener src/listener.cpp)
    
    ## Specify libraries to link a library or executable target against
    target_link_libraries(${PROJECT_NAME}_node
      ${catkin_LIBRARIES}
    )

## 5. Build last changes (on catkin_ws)

    $ catkin_make

## 6. Nodes execution (each one in a different terminal so, 3 terminals)

    $ roscore
    $ rosrun beginner_tutorials talker
    $ rosrun beginner_tutorials listener
