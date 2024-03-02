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
