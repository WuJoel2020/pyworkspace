def funOut(func):
    print("这是装饰器funOut")  # 在被装饰的函数调用之前就调用了

    def funIn(*args, **kwargs):
        print("新功能前置")
        return func(*args, **kwargs)

    return funIn

@funOut
def add(a, b, c):
    return a+b+c

print(add(1, 3, 5))