from math import hypot

class Vector:
    
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return 'Vector(%r, %r)' % (self.x, self.y)
        return 'repr'

    def __str__(self) -> str:
        return 'abc'
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y *scalar)
    
a = Vector()
print(a)

# 三种获取字符串表示形式的方式
print(repr(a))
print('%r' % a)
print('{!r}'.format(a))

print('%r %r' % (1, '1'))  # 使用%r获取对象各个属性标准字符串表示形式的好处

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)  # Vector(4, 5)

v = Vector(3, 4)
print(abs(v))