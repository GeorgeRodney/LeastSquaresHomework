import numpy as np
import matplotlib.pyplot as plt

# This is a Fox and Rabbit dynamics model. 
# x_k = [pop(fox) pop(rabbit)]^T
# u: Food input: For rabbits

F = np.array([[0.2, 0.4],
              [-0.4, 1]])

Q = np.array([[1, 0],
              [0, 2]])

u = 1000

G = np.array([[0],
              [1]])

x = np.array([[10],
              [20]])

P = np.array([[40, 0],
              [0, 40]])


for iter in range(1000):

    x = F @ x + G * u
    P = F @ P @ F.T + Q

print("x:")
print(x)
print("\n")

print("P:")
print(P)

## HEY THIS WORKED. Assuming the dynamics are correct, I arrive at a solution:
# x:
# [[2.5]
#  [5. ]]


# P:
# [[2.88085938 3.07617188]
#  [3.07617188 7.95898438]]

## LETS TRY A MASSIVE INPUT u = 1000. OK. So the state values go through the roof. The P matrix is EXACTLY the same
# x:
# [[2500.]
#  [5000.]]


# P:
# [[2.88085938 3.07617188]
#  [3.07617188 7.95898438]]

