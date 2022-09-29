import numpy as np


def Jacobi(A, b, k):
    n = A.shape[1]
    D = np.eye(n)
    D[np.arange(n), np.arange(n)] = A[np.arange(n), np.arange(n)]
    LU = D - A
    X = np.zeros(n)
    for i in range(k):
        D_inv = np.linalg.inv(D)
        X = np.dot(np.dot(D_inv, LU), X) + np.dot(D_inv, b)
    print(f'The {k} times answer：', X.tolist())
    return X


def Gauss_Seidel(A, b, k):
    n = A.shape[1]
    D = np.eye(n)
    D[np.arange(n), np.arange(n)] = A[np.arange(n), np.arange(n)]
    LU = D - A
    L = np.tril(LU)
    U = np.triu(LU)
    D_L = D - L
    X = np.zeros(n)
    for i in range(k):
        D_L_inv = np.linalg.inv(D_L)
        X = np.dot(np.dot(D_L_inv, U), X) + np.dot(D_L_inv, b)
    print(f'The {k} times answer：', X.tolist())
    return X


'''
A = np.array([
    [4, 3, 0],
    [3, 4, -1],
    [0, -1, 4]
])
b = np.array([24, 30, -24])
k = 100

A = np.array([
    [2, -1, 1],
    [1, 1, 1],
    [-1, -2, 2]
])
b = np.array([1, 2, -5])
k = 50

A = np.array([
    [1, 2, -2],
    [1, 1, 1],
    [2, 2, 1]
])
b = np.array([1,1,1])
k = 10
'''
A = np.array([
    [3, -1, 1],
    [3, 6, 2],
    [3, 3, 7]
])
b = np.array([1, 0, 4])
k = 100
print('Jacobi')
X_Jacobi = Jacobi(A, b, k)
print('Gauss_Seidel')
X_Gauss_Seidel = Gauss_Seidel(A, b, k)
