"""
函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数。
什么是高阶函数？
1. 变量可以指向函数
2. 函数名也是变量
"""

# abs()代表对函数的调用，abs是函数本身
print(abs(-10))
print(abs)

f = abs  # 变量可以指向函数
print(f(-10))  # 还可以通过该变量来调用函数

# abs=1 # 函数名也是变量，实际中变量名命名是不能这样写

"""
既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另外一个函数作为参数，
这种函数就称为高阶函数。
"""


def add(x, y, f):
    return f(x) + f(y)


print(add(-10, 5, abs))
