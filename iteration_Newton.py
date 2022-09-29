#
"""
@Author: 赵丹彪 胡长昊
@DateTime: 2022-08-27
@FileName: iteration_Newton.py
"""
#


import sympy


# 计算1-范数
def norm1(p):
    max_of_p = max(abs(p))
    return max_of_p.evalf()


# 牛顿法
def newton(funcs, x_pre, args, prec=0.0001, n=10):
    jacobianMatrix = funcs.jacobian(args)  # 计算雅可比矩阵
    for k in range(0, n):  # 迭代求解
        b = - funcs.subs(list(zip(args, x_pre)))  # 计算f（x[k]）
        J = jacobianMatrix.subs(list(zip(args, x_pre)))  # 计算雅可比矩阵Jf（x[k]）
        deltx = sympy.Matrix(J.inv() * b)  # 使用雅可比矩阵的逆求解deltx
        x_new = x_pre + deltx  # 迭代更新x
        if norm1(deltx) < prec:  # 如果满足精度要求则返回
            return x_new.evalf(), k
        x_pre = x_new
    return "迭代次数较少，无法满足精度要求"


if __name__ == "__main__":
    prec = 0.0000001  # 设置精度
    n = 20  # 设置迭代次数
    k = 0
    x = [0, 0]
    x_pre = x.copy()
    for k in range(0, n):
        x[0] = (x[0] * x[0] + x[1] * x[1] + 8) / 10
        x[1] = (x[0] * x[1] * x[1] + x[0] + 7) / 12
        for i in range(len(x_pre)):
            x_pre[i] = x_pre[i] - x[i]
        if norm1(sympy.Matrix(x)) < prec:  # 如果满足精度要求则返回
            break
        x_pre = x.copy()
    print('第一题\n‘简单迭代法’')
    print(x)
    print(f'迭代了{k}次')

    x1, x2 = sympy.symbols("x1 x2")  # 定义自变量
    args = sympy.Matrix([x1, x2])  # 定义自变量参数矩阵
    # 定义非线性方程组列表
    A = [x1 ** 2 - 10 * x1 + x2 ** 2 + 8,
         x1 * (x2 ** 2) + x1 - 12 * x2 + 7]
    funcs = sympy.Matrix(A)
    x_pre = sympy.Matrix([0] * len(A))  # 设置初始向量
    p = newton(funcs, x_pre, args, prec, n)  # 牛顿法求解
    print('牛顿法')
    print(p[0])
    print(f'迭代了{p[1]}次')

    x = [0, 0, 0]
    x_pre = x.copy()
    for k in range(0, n):
        x[0] = (x[1] * x[1] - x[0] * x[2] + 2) / 5
        x[1] = (x[2] - x[0] * x[2]) / 4
        x[2] = (x[0] * x[0] + x[1] - 1) / 3
        for i in range(len(x_pre)):
            x_pre[i] = x_pre[i] - x[i]
        if norm1(sympy.Matrix(x)) < prec:  # 如果满足精度要求则返回
            break
        x_pre = x.copy()
    print('第二题\n‘简单迭代法’')
    print(x)
    print(f'迭代了{k}次')

    x1, x2, x3 = sympy.symbols("x1 x2 x3")  # 定义自变量
    args = sympy.Matrix([x1, x2, x3])  # 定义自变量参数矩阵
    # 定义非线性方程组列表
    A = [5 * x1 - x2 ** 2 + x1 * x3 - 2,
         x1 * x3 + 4 * x2 - x3,
         x1 ** 2 + x2 - 3 * x3 - 1]
    funcs = sympy.Matrix(A)
    x_pre = sympy.Matrix([0] * len(A))  # 设置初始向量
    p = newton(funcs, x_pre, args, prec, n)  # 牛顿法求解
    print('牛顿法')
    print(p[0])
    print(f'迭代了{p[1]}次')
