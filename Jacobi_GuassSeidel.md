## 1.  The python code is:

``` python
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
        print(f'The {i + 1} times answer£º', X.tolist())
    return X


def Guass_Seidel(A, b, k):
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
        print(f'The {i + 1} times answer£º', X.tolist())
    return X


A = np.array([
    [4, 3, 0],
    [3, 4, -1],
    [0, -1, 4]
])
b = np.array([24, 30, -24])
k = 4
print('Jacobi')
X_Jacobi = Jacobi(A, b, k)
print('Guass_Seidel')
X_Guass_Seidel = Guass_Seidel(A, b, k)


```

####  This is the result of the iterative four times

```python
Jacobi
The 1 times answer£º [6.0, 7.5, -6.0]
The 2 times answer£º [0.375, 1.5, -4.125]
The 3 times answer£º [4.875, 6.1875, -5.625]
The 4 times answer£º [1.359375, 2.4375, -4.453125]
Guass_Seidel
The 1 times answer£º [6.0, 3.0, -5.25]
The 2 times answer£º [3.75, 3.375, -5.15625]
The 3 times answer£º [3.46875, 3.609375, -5.09765625]
The 4 times answer£º [3.29296875, 3.755859375, -5.06103515625]
```

####  This is the result of the iterative ten times

```python
Jacobi
The 1 times answer£º [6.0, 7.5, -6.0]
The 2 times answer£º [0.375, 1.5, -4.125]
The 3 times answer£º [4.875, 6.1875, -5.625]
The 4 times answer£º [1.359375, 2.4375, -4.453125]
The 5 times answer£º [4.171875, 5.3671875, -5.390625]
The 6 times answer£º [1.974609375, 3.0234375, -4.658203125]
The 7 times answer£º [3.732421875, 4.8544921875, -5.244140625]
The 8 times answer£º [2.359130859375, 3.3896484375, -4.786376953125]
The 9 times answer£º [3.457763671875, 4.5340576171875, -5.152587890625]
The 10 times answer£º [2.599456787109375, 3.6185302734375, -4.866485595703125]
Guass_Seidel
The 1 times answer£º [6.0, 3.0, -5.25]
The 2 times answer£º [3.75, 3.375, -5.15625]
The 3 times answer£º [3.46875, 3.609375, -5.09765625]
The 4 times answer£º [3.29296875, 3.755859375, -5.06103515625]
The 5 times answer£º [3.18310546875, 3.847412109375, -5.03814697265625]
The 6 times answer£º [3.11444091796875, 3.904632568359375, -5.023841857910156]
The 7 times answer£º [3.0715255737304688, 3.9403953552246094, -5.014901161193848]
The 8 times answer£º [3.044703483581543, 3.962747097015381, -5.009313225746155]
The 9 times answer£º [3.0279396772384644, 3.976716935634613, -5.005820766091347]
The 10 times answer£º [3.0174622982740402, 3.985448084771633, -5.003637978807092]

```

 From here we see that Guass-Seidel iterative method is better than Jacobi method.

## 2. 

### The first question

#### This is the result of the iterative ten times

```python
Jacobi
The 50 times answer£º [-514083.062613634, -2633749.231906023, 1062924.3916259394]
Gauss_Seidel
The 50 times answer£º [1.4, 1.2000000000000002, -0.5999999999999999]
```

The obvious Gauss-Seidel iterative method get the  correct answer.

### The first question

#### This is the result of the iterative ten times

```python
Jacobi
The 10 times answer£º [-3.0, 3.0, 1.0]
Gauss_Seidel
The 10 times answer£º [-11779.0, 12291.0, -1023.0]
```

The obvious Jacobi iterative method get the  correct answer.

## 3.



