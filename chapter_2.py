from math import cos, exp


def f_1(x):
    return x ** 0.5 - cos(x)


def f_2(x):
    return x ** 3 - 2 ** (-x)


def f_3(x):
    return exp(x) + 2 ** (-x) + 2 * cos(x) - 6


def f_4(x):
    return exp(x) - x ** 3 + 3 * x - 2


def f_5(x):
    return x ** 2 - 3


def get_answer(f, a, b, error=0.0001):
    c = (a + b) / 2
    while abs(f(c)) > error:
        if f(a) * f(c) > 0:
            a = c
        else:
            b = c
        c = (a + b) / 2
    return c


if __name__ == '__main__':
    print("The first answer is ", get_answer(f_1, 0, 1))
    print("The second answer is ", get_answer(f_2, 0, 1))
    print("The third answer is ", get_answer(f_3, 1, 2))
    print("The fourth answer is ", get_answer(f_4, 0, 1))
    print("The fifth answer is ", get_answer(f_5, 1, 2))
