from unicodedata import decimal
import numpy as np

a = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])

# (i) integer elements only 
result1 = a[a == a.astype(int)]
print ("Integer Elements only : ", result1)

# (ii) float elements only
print ("Float Elements only : ", a[a != a.astype(int)])