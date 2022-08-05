import numpy as np

# i
x = np.array([1,2,3,4,5,1,2,1,1,1])
print("Most frequently occuring element is = ", np.bincount(x).argmax());

# ii
y = np.array([1,1,1,2,3,4,2,4,3,3])
print("Most frequently occuring element is = ", np.bincount(y).argmax());
