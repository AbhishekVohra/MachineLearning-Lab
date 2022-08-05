import numpy as np

a = np.array([10,52,62,16,16,54,453])

# (i) sorted array
print ("Sorted array : ", np.sort(a))

# (ii) indices of sorted array
print ("Indices of sorted array : ", np.argsort(a))

# (iii) 4 smallest elements
a = np.sort(a)
print ("4 smallest elements : ", a[:4])

# (iv) 5 largest elements
print ("5 largest elements : ", a[-5:])