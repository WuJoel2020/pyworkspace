# 一个函数f(x)=x^2，要把这个函数作用在一个list[1, 2, 3, 4, 5]
def f(x):
    return x * x


a = [1, 2, 3, 4, 5]
it = map(f, a)  # 返回的it是一个可迭代的对象
print(type(it))
# 判断是否是可迭代的对象
from collections.abc import Iterator

print("判断是否是可迭代的：", isinstance(it, Iterator))
print(list(it))

# 将列表中每个元素转换为字符串
print(list(map(str, a)))

# map传递多个列表
b = [10, 20, 30]


def f(x, y):
    return x + y


print(list(map(f, a, b)))  # 结果的长度会取最小
