# Control real Turtlebot from keyboard

## Dependencies:
1. ROS's Turtlebot library already installed. If it is not, try:

    $ sudo apt-get install -y ros-kinetic-turtlebot    

2. Two computers:

    1. One on Turtlebot (LSA's laptop)
    2. Other to remotely control Turtlebot (computer2)

## 1. Turn Turtlebot ON
## 2. Connect Turtlebot on a LSA's already configured laptop (lsa-geronimo)
## 3. Connect both computers on the lsa_robot WiFi network
## 4. run on LSA's laptop (terminal 1):
    $ roscore
## 5. run on LSA's laptop (terminal 2):
    $ roslaunch turtlebot_bringup minimal.launch
## 6. run on computer2:

    # LSA's laptop network address
    $ export ROS_MASTER_URI = http://192.168.0.102:11311

    # computer2 network address
    $ export ROS_HOSTNAME  =192.168.0.101

## 7. run on computer2(**new** terminal 3):

    roslaunch turtlebot_teleop keyboard_teleop.launch

## 8. Enjoy