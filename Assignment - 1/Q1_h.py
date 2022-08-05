import numpy as np

x = np.array([[2,3,4],[3,2,9]])
y = np.array([[1,5,0],[5,10,3]])

# Inner Product
print("Inner Product = ", np.inner(x,y))

# Outer Product
print("Outer Product = ", np.outer(x,y))

# Cartesian Product
print("Cartesian Product = ", np.cross(x,y))