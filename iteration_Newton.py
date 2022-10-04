"""
@Author: 赵丹彪 胡长昊
@DateTime: 2022-08-27
@FileName: iteration_Newton.py
"""

import sympy


# 计算无穷范数
def norm(p):
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
        if norm(deltx) < prec:  # 如果满足精度要求则返回
            return x_new.evalf(), k
        x_pre = x_new
    return "迭代次数较少，无法满足精度要求"


if __name__ == "__main__":
    prec = 0.0000001  # 设置精度
    n = 20  # 设置迭代次数
    k = 0
    # 不动点迭代法
    x = [0, 0]
    x1 = x[0]
    x2 = x[1]
    for k in range(0, n):
        x_pre = [x1, x2]
        x1 = (x1 * x1 + x2 * x2 + 8) / 10
        x2 = (x1 * x2 * x2 + x1 + 7) / 12
        x_pre = [x_pre[0] - x1, x_pre[1] - x2]
        if norm(sympy.Matrix(x_pre)) < prec:  # 如果满足精度要求则返回
            break
    print('第一题\n‘简单迭代法’')
    print(x1, x2)
    print(f'迭代了{k}次')

    x1, x2 = sympy.symbols("x1 x2")  # 定义自变量
    args = sympy.Matrix([x1, x2])  # 定义自变量参数矩阵
    # 定义非线性方程组列表
    A1 = [x1 ** 2 - 10 * x1 + x2 ** 2 + 8,
          x1 * (x2 ** 2) + x1 - 12 * x2 + 7]
    funcs1 = sympy.Matrix(A1)
    x_pre = sympy.Matrix([0] * len(A1))  # 设置初始向量
    p = newton(funcs1, x_pre, args, prec, n)  # 牛顿法求解
    print('牛顿法')
    print(p[0])
    print(f'迭代了{p[1]}次')

    x = [0, 0, 0]
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    for k in range(0, n):
        x_pre = [x1, x2, x3]
        x1 = (x2 * x2 - x1 * x3 + 2) / 5
        x2 = (x3 - x1 * x3) / 4
        x3 = (x1 * x1 + x2 - 1) / 3
        x_pre = [x_pre[0] - x1, x_pre[1] - x2]
        if norm(sympy.Matrix(x_pre)) < prec:  # 如果满足精度要求则返回
            break
    print('第二题\n‘简单迭代法’')
    print(x1, x2, x3)
    print(f'迭代了{k}次')

    x1, x2, x3 = sympy.symbols("x1 x2 x3")  # 定义自变量
    args = sympy.Matrix([x1, x2, x3])  # 定义自变量参数矩阵
    # 定义非线性方程组列表
    A2 = [5 * x1 - x2 ** 2 + x1 * x3 - 2,
          x1 * x3 + 4 * x2 - x3,
          x1 ** 2 + x2 - 3 * x3 - 1]
    funcs2 = sympy.Matrix(A2)
    x_pre = sympy.Matrix([0] * len(A2))  # 设置初始向量
    p = newton(funcs2, x_pre, args, prec, n)  # 牛顿法求解
    print('牛顿法')
    print(p[0])
    print(f'迭代了{p[1]}次')
