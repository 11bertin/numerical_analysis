a = [[1, 1, -1], [1, 2, 4], [2, -1, 2]]
b = [1, 2, 3]
n = len(a)
x = [0] * n


def gauss():
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            c = -a[j][i] / a[i][i]
            for k in range(0, n):
                a[j][k] += a[i][k] * c
            b[j] += b[i] * c
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            b[i] -= a[i][j] * x[j]
        x[i] = b[i] / a[i][i]


gauss()
print(x)