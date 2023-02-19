from functools import reduce

ls = [1, 2, 3, 4, 5]


# 计算一个序列的求和
def sumTest(x, y):
    return x + y


print("reduce计算列表求和:", reduce(sumTest, ls))


# 把序列[1, 2, 3, 4, 5]变成整数12345
def fun(x, y):
    return x * 10 + y


print(reduce(fun, ls))
