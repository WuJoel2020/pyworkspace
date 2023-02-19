"""
闭包的表现
a. 要有函数的嵌套（外部函数、内部函数）
b. 内部函数中使用外部函数的变量
c. 外部函数必须有返回值，返回内部函数名
"""


# 使用闭包，完成求两个数的和
def funOut(n1):
    def funIn(n2):
        nonlocal n1  # 内部函数修改外部函数的变量
        n1 += 100
        return n1 + n2

    return funIn


f = funOut(10)
print(f(20))


# 闭包求两点距离
import math


def getDisOut(x1, y1):
    def getDisIn(x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return getDisIn


getDisIn = getDisOut(0, 0)
print(getDisIn(1, 1))


# 闭包的特殊用途：不修改源代码的前提下，添加新功能
def fun1():
    print("功能1")


def funOut(func):
    def funIn():
        print("新功能前置")
        func()
        print("新功能后置")

    return funIn


fun1()
print("-----------使用闭包----------")
fun1 = funOut(fun1)
fun1()
