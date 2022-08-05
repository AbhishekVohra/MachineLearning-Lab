import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])

print(f"Array 1 = {arr1}")
print(f"Array 2 = {arr2}")

# is greater comparison
print("arr1 > arr2")
print(np.greater(arr1,arr2))

# is greater than equal to comparison
print("arr1 >= arr2")
print(np.greater_equal(arr1,arr2))

# is less than comparison
print("arr1 < arr2")
print(np.less(arr1,arr2))

# is less than equal to comparison
print("arr1 <= arr2")
print(np.less_equal(arr1,arr2))

# is equal to comparison
print("arr1 = arr2")
print(np.equal(arr1,arr2))


# another method to check equality
if (np.array_equal(arr1,arr2)):
    print("arr1 == arr2")

else:
    print("They are not equal")



