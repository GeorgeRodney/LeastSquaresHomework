import numpy as np
import matplotlib.pyplot as plt

# measurements (1,1) , (2,1), (3,1), (4,1)
meas = np.array([1,1,2,1,3,1,4,1])
x = np.zeros((4,1))

H = np.array([[1,0,1,0],
              [0,1,0,1],
              [1,0,2,0],
              [0,1,0,2],
              [1,0,3,0],
              [0,1,0,3],
              [1,0,4,0],
              [0,1,0,4]])

H_trans = H.T

S = H_trans @ H
x = np.linalg.inv(S) @ H_trans @ meas


print(f"H = \n{x}\n")

#### WOAH. This actually worked. I essentially gave this a truth object starting at (0,1) and moving with x velo = 1 and y velo = 0
#### Therefore. After 4 time steps you will be at (x,y) cord (4,1)
#### This estimate the initial position and the initial velocity. X_estimated = (x, y, xVel, yVelo) it did (0,1, 1, 0) Which is actually correct. 

#### I just cant get over how well this works

