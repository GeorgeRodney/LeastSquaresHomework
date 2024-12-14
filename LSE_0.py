import numpy as np

z = np.array([0.1, 0.9, 2.2, 3.0, 4.1])
t = np.array([0, 1, 2, 3, 4])

rows = 5
cols = 2
H = np.zeros((rows,cols))
R = np.zeros((5,5))

R[0][0] = 0.04
R[1][1] = 0.01
R[2][2] = 0.09
R[3][3] = 0.04
R[4][4] = 0.01

H[0][0] = 1
H[1][0] = 1
H[2][0] = 1
H[3][0] = 1
H[4][0] = 1

H[0][1] = 0
H[1][1] = 1
H[2][1] = 2
H[3][1] = 3
H[4][1] = 4

# With R
R_inv = np.linalg.inv(R)
Htrans_Rinv_H = H.T @ R_inv @ H
X0 = np.linalg.inv(Htrans_Rinv_H) @ H.T @ R_inv @ z

# Without R
# Htrans_H = H.T @ H
# X0 = np.linalg.inv(Htrans_H) @ H.T @ z

TIME = np.array([1, 1])

X_1 = TIME.T @ X0
X = np.array([X_1, 1])

X_2 = TIME.T @ X
X = np.array([X_2, 1])

X_3 = TIME.T @ X
X = np.array([X_3, 1])

X_4 = TIME.T @ X

Error = np.array([X0[0], X_1, X_2, X_3, X_4])
Error = z - Error
ErrorTrans = Error.T

J = ErrorTrans @ R_inv @ Error

print("Meaurements: ", z)
print("Initial Position and Velocity", X0)
print("X_1:", X_1)
print("X_2:",X_2)
print("X_3:",X_3)
print("X_4:",X_4)
print("\n")