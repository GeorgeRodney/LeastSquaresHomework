import numpy as np
import matplotlib.pyplot as plt

F = np.array([[0, 1],
              [0, 0]])

P = np.array([[1,0],
     [0,0]])

Q = np.array([[1, 0],
     [0, 0]])

angle = []
angleRate = []

angle.append(P[0, 0])
angleRate.append(P[1, 1])

ITERATIONS = 100
for iter in range(ITERATIONS):

    P = F @ P @ F.T + Q
    angle.append(P[0, 0])
    angleRate.append(P[1, 1])

time = range(ITERATIONS+1)

plt.figure(figsize=(10, 5))
plt.plot(time, angle, label='P00')
plt.plot(time, angleRate, label='P11')
plt.xlabel('Time Step')
plt.ylabel('State Value')
plt.title('Position and Velocity over Time')
plt.ylim([-4, 4])
plt.legend()
plt.grid()
plt.show()