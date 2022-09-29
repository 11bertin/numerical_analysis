import numpy as np

A = np.array([[1, 1, 0, 0],
              [2, -1, 5, 0],
              [0, 3 - 4, 2],
              [0, 0, 2, 6]])
f = np.array([5, -9, 19, 2])

a = np.array([0, 1, 1, 1, 1], dtype=float)
b = np.array([4, 4, 4, 4, 4], dtype=float)
c = np.array([1, 1, 1, 1, 0], dtype=float)
y = np.zeros(5)
B = np.zeros(5)
x = np.zeros(5)
y[0] = f[0] / b[0]
d = b[0]
for i in range(1, 4):
    B[i - 1] = c[i - 1] / d
    d = b[i] - a[i] * B[i - 1]
    y[i] = (f[i] - a[i] * y[i - 1]) / d
x[4] = y[4]

for i in range(3, -1, -1):
    x[i] = y[i] - B[i] * x[i + 1]
print('追赶法：', x)
