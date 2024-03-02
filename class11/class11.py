from nptyping import NDArray, Shape, UInt64
import numpy as np

data: NDArray[Shape["10"], UInt64] = np.arange(1, 10).astype(UInt64)
print(data)
data2 = data + 5
print(data2)

a: NDArray[Shape["*, *"], UInt64] = np.array([[1, 2, 3, 4],
                                            [5, 6, 7, 8],
                                            [9, 10, 11, 12],])
print(a)
b: NDArray[Shape["*, *"], UInt64] = np.array([[1, 2, 3],
                                            [5, 6, 7],
                                            [9, 10, 11],])
print(b)
c: NDArray[Shape["*, *"], UInt64] = np.array([[1, 2],
                                            [5, 6],
                                            [9, 10],])
print(c)

# Reshape a NumPy array of shape (4, 3) into a 1D array.
arr2: NDArray[Shape["Size, Size"],UInt64] = np.arange(4*3).reshape(4,3).astype(UInt64)
print(arr2)

# Given a NumPy array arr = np.array([1, 2, 3, 4, 5]), find the index of the maximum value.
arr1: NDArray[Shape["5"], UInt64] = np.array([1,2,3,4,5])
print(arr1.argmax())

# Normalize the values in a NumPy array arr so that they range between 0 and 1.
arr3: NDArray[Shape["5"], UInt64] = np.array([1,2,3,4,5])
print(arr3/arr3.max())

# Compute the dot product of two NumPy arrays arr1 = np.array([1, 2, 3]) and arr2 = np.array([4, 5, 6]).
arr4: NDArray[Shape["5"], UInt64] = np.array([1, 2, 3,4])
arr5: NDArray[Shape["5"], UInt64] = np.array([1,2,3,5])
print(np.dot(arr4,arr5))
