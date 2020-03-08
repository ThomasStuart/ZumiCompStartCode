# https://github.com/ArN5/zumi_samples/blob/master/zumi_speed_calibration.ipynb
#this code was made for the original zumi field v1
#the field was a grid spaced 43 cm every node.

from zumi.zumi import Zumi
import time
import math

speed_set = 40 #zumi speed set percent of battery to motor
speed_cm_sec  = 15.24 #6 inches
slope_int = 2.54 #1 inch


# this function will move Zumi in the desired
# angle for a certain distance
# the accuracy of the distance traveled
# is predicted by the given
# predicted speed and predicted y intercept
def move_cm(distance, angle):
    global speed_set, speed_cm_sec, slope_int

    speed = speed_set
    slope = speed_cm_sec
    y_intercept = slope_int

    # this is the speed Zumi
    # travels at, in centimeters per second

    # how much time in seconds
    # it takes to travel the distance in inches
    duration = (distance - y_intercept) / slope

    # make sure if there is no distance only turn
    if (distance < 1):
        zumi.turn(angle)
    # if there is a distance go at speed 40 at that angle
    else:
        # time.time returns the current time in seconds
        time_start = time.time()
        time_elapsed = 0
        while (duration > time_elapsed):
            # update the time that has passed
            time_elapsed = time.time() - time_start
            # take a step in that direction going forward
            zumi.go_straight(speed, angle)

        # once done stop zumi
        zumi.hard_brake()

def route():
    pass


#create the Zumi object
zumi = Zumi()

#Recablibrate Zumi just in case
zumi.mpu.calibrate_MPU()

#reset the gyro list
zumi.reset_gyro()

#initiate our starting location to 0,0
current_x = 0
current_y = 0
#you must point Zumi at the X axis. this will be 0 degrees

try:
    route()
finally:
    zumi.stop()
