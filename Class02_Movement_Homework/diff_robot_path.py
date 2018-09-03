# source: http://www.swarthmore.edu/NatSci/mzucker1/e28_f2016/hw1_starter.py
# starter code for E28 homework 1 problem 3
import numpy as np
import matplotlib.pyplot as plt

# start the robot out at 0,0,0
(x, y, theta) = (0, 0, 0)

# simulate for this amount of time
t_final = 10.0 

# set a reasonable delta t
delta_t = 0.125 

# start at t = 0
t = 0.0 

# robot parameters
r = 0.05 # wheels have 5cm radius
d = 0.10 # wheels 20cm apart

# start a list of x/y pairs to plot
all_points = [ (x, y) ]

# simulate the desired amount of time
while t < t_final:

    # get left/right wheel velocities (rad/sec). these are currently
    # constant, but they could be time-varying
    (vl, vr) = (0, 2.0)

    # diff drive kinematics update
    linear_vel = (vl + vr)*r/2.0
    angular_vel = (vr - vl)*r/(2.0*d)

    # Euler's method update
    x += delta_t * linear_vel * np.cos(theta)
    y += delta_t * linear_vel * np.sin(theta)
    theta += delta_t * angular_vel
    
    # time update
    t += delta_t

    # add x, y point
    all_points.append( (x, y) )

# convert points to numpy array so we can do 2D indexing like below
all_points = np.array(all_points)

# plot using red lines with x's
plt.plot(all_points[:,0], all_points[:,1], 'rx-')

# make sure circles look like circles
plt.axis('equal')

# show the plot
plt.show()