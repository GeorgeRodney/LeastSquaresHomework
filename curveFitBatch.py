import numpy as np
import matplotlib.pyplot as plt

# Create measurements [y]
size = 10
mean = 0
std_dev = 0.5
base_array = np.linspace(1, 10, size)
noise = np.random.normal(mean, std_dev, size)
y = base_array + noise
y_col = y.reshape(-1,1)

t = np.array([1, 2, 3 ,4, 5, 6, 7, 8, 9, 10])
x = np.zeros((2,1))

H = np.array([[1,1],
              [1,2],
              [1,3],
              [1,4],
              [1,5],
              [1,6],
              [1,7],
              [1,8],
              [1,9],
              [1,10]])

H_trans = H.T

S = H_trans @ H
x = np.linalg.inv(S) @ H_trans @ y_col


print(f"H = \n{x}\n")

#### SHE WORKS. This gives you a good estimate as well. Just like the recursive.
#### The advantage being that this is simpler to implement but is less useful. The real world is real time!!!!!
