import numpy as np

# (i)

p = [[1,2],[2,3]]
q = [[4,5],[6,7]]

print("Product of the two matrices = ", np.matmul(p,q))

print("Covariance between the two matrices = ", np.cov(p,q))


# (ii)

p1 = [[1,2],[2,3],[4,5]]
q1 = [[4,5,1],[6,7,2]]

print("Product of the two matrices = ", np.matmul(p1,q1))
# the line below produces error
# because covariance can be calculate for matrices of same dimensions only
# print("Covariance between the two matrices = ", np.cov(p1,q1))
