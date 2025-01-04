import numpy as np
from scipy.linalg import expm

# Define constants and matrices
A = np.array([[-0.5, 0],
              [0, -1]])  # System matrix

t_k = 0.0        # Current time
t_k1 = 0.5       # Next time step
tau = t_k1 - t_k # Time horizon (delta time)
N = 100          # Number of integration steps

# Define Q_c(tau) (time-varying process noise covariance)
def Q_c(tau):
    return np.array([[1 + 0.1 * tau, 0],
                     [0, 1 + 0.1 * tau]])

# Numerical integration
dt = tau / N  # Time step
Q_k1 = np.zeros_like(A, dtype=float)  # Initialize the process noise covariance

for i in range(N + 1):
    current_tau = t_k + i * dt  # Calculate current time in integration
    exp_A = expm(A * (t_k1 - current_tau))  # e^(A(t_{k+1} - tau))
    exp_A_T = exp_A.T  # Transpose
    Q_c_tau = Q_c(current_tau)  # Q_c(tau)
    
    # Accumulate the integral
    Q_k1 += exp_A @ Q_c_tau @ exp_A_T * dt

print("Process noise covariance Q_k+1:\n", Q_k1)
