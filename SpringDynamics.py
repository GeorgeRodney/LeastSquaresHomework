import matplotlib.pyplot as plt
import numpy as np

k = 1

F = np.array([[0, 1],
              [-k, 0]])

x = np.array([[3],
              [0]])

pos = []
vel = []

pos.append(x[0,0])
vel.append(x[1,0])
ITERATIONS = 100
for iter in range(ITERATIONS):

    x = F @ x
    pos.append(x[0, 0])
    vel.append(x[1, 0])

time = range(ITERATIONS+1)

plt.figure(figsize=(10, 5))
plt.plot(time, pos, label='Position (x1)')
plt.plot(time, vel, label='Velocity (x2)')
plt.xlabel('Time Step')
plt.ylabel('State Value')
plt.title('Position and Velocity over Time')
plt.ylim([-4, 4])
plt.legend()
plt.grid()
plt.show()