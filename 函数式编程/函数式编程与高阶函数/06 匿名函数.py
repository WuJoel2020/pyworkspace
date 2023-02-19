# lambda arg1, arg2... : 表达式
f = lambda a, b, c: a + b + c
print("调用", f(3, 4, 5))

# 匿名函数作为map高阶函数的参数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))


# sorted中使用匿名函数
class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def __repr__(self) -> str:
        return self.name

stu1 = Student("zhangsan", 21)
stu2 = Student("lisi", 25)
stu3 = Student("wangwu", 23)
print(sorted([stu1, stu2, stu3], key=lambda x: x.age))
