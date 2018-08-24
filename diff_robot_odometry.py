print "***** Robot Design Constants Definition *****"
distance_btwn_wheels            =   input('Please, insert the distance between the robot wheels (m)     : ')
encoder_ticks_per_revolution    =   input('Please, insert the encoder`s number of ticks per revolution  : ')
wheel_radius                    =   input('Please, insert the robot`s wheel radius (m)                  : ')
print "***** Current Robot Position *****"
robot_current_x_pos             =   input('Please, insert robot current X position  :')
robot_current_y_pos             =   input('Please, insert robot current Y position  :')
robot_current_angle             =   input('Please, insert robot current angle (rad) :')


velocity_left           =   2*x_linear_vel - z_angular_ang*distance_btwn_wheels
velocity_right          =   2*x_linear_vel + z_angular_ang*distance_btwn_wheels

print "Velcoity left:   ", velocity_left
print "Velcoity right:  ", velocity_right
