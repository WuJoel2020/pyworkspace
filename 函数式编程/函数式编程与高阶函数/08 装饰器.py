# 装饰器的基本使用
def funOut(func):
    print("这是装饰器funOut")  # 在被装饰的函数调用之前就调用了

    def funIn():
        print("新功能前置")
        func()
        print("新功能后置")

    return funIn


@funOut
def fun1():
    print("功能1")


print("准备调用装饰过的fun1")
fun1()

## 多个装饰器
print("--------------多个装饰器-------------")


def funOut1(func):
    print("这是装饰器funOut1")  # 在被装饰的函数调用之前就调用了

    def funIn():
        print("funOut1新功能前置")
        func()
        print("funOut1新功能后置")

    return funIn


@funOut1  # 注意顺序，内层函数外的语句，从下置上。内层函数内的语句，从上置下。
@funOut  # 包装时先包里面的，拆开时先拆外面的。
def fun1():
    print("功能1")


print("准备调用装饰过的fun1")
fun1()
