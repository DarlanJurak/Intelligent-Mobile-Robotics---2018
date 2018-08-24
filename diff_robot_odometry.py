import math

print "***** Robot Design Constants Definition *****"
robot_distance_btwn_wheels              =   input('Please, insert the distance between the robot wheels (m)     : ')
robot_encoder_ticks_per_revolution      =   input('Please, insert the encoder`s number of ticks per revolution  : ')
robot_wheel_radius                      =   input('Please, insert the robot`s wheel radius (m)                  : ')
print "***** Robot Initial  Position *****"
robot_initial_x_pos                     =   input('Please, insert robot initial X position                      : ')
robot_initial_y_pos                     =   input('Please, insert robot initial Y position                      : ')
robot_initial_angle                     =   input('Please, insert robot initial angle (rad)                     : ')
print "***** Robot Current Position *****"  
robot_encoder_current_ticks_left         =   input('Please, insert robot current ticks - left -                 : ')
robot_encoder_current_ticks_right        =   input('Please, insert robot current ticks - right -                : ')

print "***** Robot Current X, Y, Angle Position Calculation *****"
print " ... "
distance_right                          =   2*math.pi*robot_wheel_radius*robot_encoder_current_ticks_right/robot_encoder_ticks_per_revolution
distance_left                           =   2*math.pi*robot_wheel_radius*robot_encoder_current_ticks_left/robot_encoder_ticks_per_revolution
distance_center                         =   (math.pi*robot_distance_btwn_wheels/robot_encoder_ticks_per_revolution)*(robot_encoder_current_ticks_right + robot_encoder_current_ticks_left)

robot_current_x_pos                     =   robot_initial_x_pos + distance_center * math.cos(robot_initial_angle)
robot_current_y_pos                     =   robot_initial_y_pos + distance_center * math.sin(robot_initial_angle)
robot_current_angle                     =   robot_initial_angle + (distance_right - distance_left)/robot_distance_btwn_wheels

print "***** Robot Current Position *****"
print "Robot Current X pos: ", robot_current_x_pos
print "Robot Current Y pos: ", robot_current_y_pos
print "Robot Current angle: ", robot_current_angle

