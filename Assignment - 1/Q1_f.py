import numpy as np

n_array = np.array([[55,25,15],[30,44,2],[11,45,77]])

# (i) Sum of diagonal elements
print("Sum of diagonal elements of the Matrix = ", np.trace(n_array))

a, b = np.linalg.eig(n_array)
# (ii) Eigen values of matrix
print("Eigen Values of the Matrix are = ", a)

# (iii) Eigen Vectors of the Matrix
print("Eigen Vectors of the Matrix are = ", b)

# (iv) Inverse of the matrix
print("Inverse of Matrix = ", np.linalg.inv(n_array))

# (v) Determinant of the matrix
print("Determinant of matrix = ", np.linalg.det(n_array))