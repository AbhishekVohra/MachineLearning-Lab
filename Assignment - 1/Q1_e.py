import numpy as np

gfg = np.matrix('[4,1,9; 12,3,1; 4,5,6]')

# (i) Sum Of all Elements
print("Sum of all elements of matrix = ", gfg.sum())

# (ii) Sum of all Elements Row-wise
print("Sum of all Elements Row-wise = ", gfg.sum(axis=1))

# (iii) Sum of all Elements Column-wise
print("Sum of all Elements Columns-wise = ", gfg.sum(axis=0))