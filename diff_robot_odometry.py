print "***** Robot Design Constants Definition *****"
x_linear_vel            =   input('Please, insert x linear velocity                     (m/s): ')
z_angular_ang           =   input('Please, insert z angular velocity                    (rad): ')
distance_btwn_wheels    =   input('Please, insert the distance between the robot wheels (m)  : ')

velocity_left           =   2*x_linear_vel - z_angular_ang*distance_btwn_wheels
velocity_right          =   2*x_linear_vel + z_angular_ang*distance_btwn_wheels

print "Velcoity left:   ", velocity_left
print "Velcoity right:  ", velocity_right