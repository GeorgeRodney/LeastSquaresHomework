import numpy as np
import matplotlib.pyplot as plt

# Create measurements [y]
x = np.array([1000, -10, -9.81/2])
k = np.linspace(1,100,100)
y = x[0] + x[1]*k + x[2]*k*k

mean = 0
std_dev = 0.5
size = 100
noise = np.random.normal(mean, std_dev, size)
noise_y = y + noise

# print(f"Y = \n{y}\n")
# print(f"noisey Y = \n{noise_y}\n")

# Set the number of rows (100) and the range for t values (from 1 to 100)
size = 100
t_values = np.arange(1, size+1)  # t values from 1 to 100

# Create the H matrix where each row is [1, t, t^2]
H = np.column_stack([np.ones(size), t_values, t_values**2])
# print(H)

## NOW ESTIMATE THE PARAMETERS

S = H.T @ H

# x_est = np.linalg.inv(S) @ H.T @ noise_y
x_est = np.linalg.inv(S) @ H.T @ y

print(x_est)

###### WOW!  x_nought actual = [1000, -10, -9.81/2]

#####        x_estimated = [1000.     -10.      -4.905]
##### I mean. Its perfect. This is clearly optimal with no noise
