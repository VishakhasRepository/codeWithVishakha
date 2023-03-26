import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def sumDiagonal(a):
    sum = 0
    for i in range(0, len(a)):  # runs three times
        sum = sum + a[i][i]
        # print(a[i][i])
    print(sum)


sumDiagonal(arr1)
