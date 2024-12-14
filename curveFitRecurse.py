import numpy as np
import matplotlib.pyplot as plt

# Create measurements [y]
size = 10
mean = 0
std_dev = 0.5
base_array = np.linspace(1, 10, size)
noise = np.random.normal(mean, std_dev, size)
y = base_array + noise

t = np.array([1, 2, 3 ,4, 5, 6, 7, 8, 9, 10])
R = 0.25
x = np.array([[1], [0]])
P = np.array([[1, 0], [0, 1]])
x_perf = np.zeros((11,2,1))
P00 = np.zeros((11,1))
P11 = np.zeros((11,1))

P00[0] = P[0][0]
P11[0] = P[1][1]
x_perf[0] = x

k = np.linspace(0,10, 100)
# z = np.zeros((11, 1, 100))
# z[0] = x[0] + x[1]*k

for time in range(len(t)):

    print(f"At time {t[time]}:")
    H = np.array([[1, t[time]]])

    H_trans = H.T
    S = H @ P @ H_trans + R
    K = P @ H_trans @ np.linalg.inv(S)
    # print(f"K =\n{K}\n")

    residual = y[time] - H @ x
    # print(f"residual =\n{residual}\n")
    # print(f"PRE X = \n{x}\n")
    x = x + K @ residual
    x_perf[time+1] = x
    print(f"POST X = \n{x}\n")

    # Create Line from State
    # z[time+1] = x[0] + x[1] * k
    # print(f"z[time+1] = \n{z[time+1]}\n")

    P = (np.array([[1, 0], [0, 1]]) - K @ H) @ P
    P00[time+1] = P[0][0]
    P11[time+1] = P[1][1]
    # print(f"P = \n{P}\n")

# print(f"x perf = \n{x_perf}\n")
# print(f"P00 = \n{P00}\n")

t = np.array([0, 1, 2, 3 ,4, 5, 6, 7, 8, 9, 10])
plt.figure(1)

plt.title("Estimated X")
z = x[0] + x[1] * k
plt.plot(k, z, label=f"Line: y = {x[1]}x + {x[0]}", color='b')
# plt.plot(k, z[10], label=f"Line: y = {0}x + {1}", color='r')
plt.legend()

plt.figure(2)
plt.subplot(2,1,1)
plt.title("x1 std")
plt.plot(t, np.sqrt(P00), marker='o', linestyle='-', color='b')

plt.subplot(2,1,2)
plt.title("x2 std")
plt.plot(t, np.sqrt(P11), marker='o', linestyle='-', color='g')

plt.show()


### THIS WORKS. Same as the batch estimation. The advantage is that she is REAL TIME
### Disadvantage being that this is more complicated to implement. More calcs. 

