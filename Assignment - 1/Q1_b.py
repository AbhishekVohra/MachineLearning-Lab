import numpy as np

array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])

# Method - 1 (using flatten method)
# Row Major Flattening
array2 = array1.flatten('C')
print(array2)

# Column Major Flattening
array3 = array1.flatten('F')
print(array3)


# Method - 2 (using reshape method)
array4 = array1.reshape(-1)
print(array4)

