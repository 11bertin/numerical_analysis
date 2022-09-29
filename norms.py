import numpy as np

a = [3, -4, 0, 1.5]
print('向量a:', a)
print('向量a的1-范数', a)
print(np.linalg.norm(a, ord=1))
print('向量a的2-范数:')
print(np.linalg.norm(a, ord=2))
print('向量a的∞-范数:')
print(np.linalg.norm(a, ord=np.inf))
print('\n\n')
b = [2, 1, -3, 4]

print('向量b:', b)
print('向量b的1-范数', b)
print(np.linalg.norm(b, ord=1))
print('向量b的2-范数:')
print(np.linalg.norm(b, ord=2))
print('向量b的∞-范数:')
print(np.linalg.norm(b, ord=np.inf))
