import numpy as np

# y = x^2
# integral: y from 0 to 1

t_k = 0
t_k1 = 1
delta = t_k1 - t_k

N = 100000000
dt = delta / N
sum = 0
print("Iterations:")
print(N)

for idx in range(N):

    k = idx / N
    y = k**2 * dt

    sum = sum + y

print(sum)