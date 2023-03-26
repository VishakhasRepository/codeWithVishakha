import numpy as np

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

#print(matrix)

def rotateMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            print(matrix[i,j])


rotateMatrix(matrix)