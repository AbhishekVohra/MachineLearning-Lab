import numpy as np

array1 = np.array([[1,-2,3],[-4,5,-6]])

# (i) element wise absolute value
print("Element wise absolute value = ", np.absolute(array1))

# (ii) Percentile
np.ndarray.flatten(array1)


print("25th percentile along every row : ", np.percentile(array1, 25, axis=1))
print("25th percentile along every column : ", np.percentile(array1, 25, axis=0))


print("50th percentile along every row : ", np.percentile(array1, 50, axis=1))
print("50th percentile along every column : ", np.percentile(array1, 50, axis=0))


print("75th percentile along every row : ", np.percentile(array1, 75, axis=1))
print("75th percentile along every column : ", np.percentile(array1, 75, axis=0))


# (iii) Mean Median Mode

print("Mean of each Column : ", np.mean(array1,axis=0))
print("Mean of each Row : ", np.mean(array1,axis=0))

print("Median of each Column : ", np.median(array1,axis=0))
print("Median of each Row : ", np.median(array1,axis=0))

print("Standard Deviation of each Column : ", np.std(array1,axis=0))
print("Standard Deviation of each Row : ", np.std(array1,axis=0))