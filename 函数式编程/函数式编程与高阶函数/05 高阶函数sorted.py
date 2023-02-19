# 对数值排序
ls = [42, 422, 4, 2, -100, 3, -10]
print("默认升序排序", sorted(ls))

# 逆序排序
print("逆序排序", sorted(ls, reverse=True))

# 对字符串排序，参考 ASCII 码
strls = ["abc", "ABC", "D", "d", "C"]
print("字符串排序", sorted(strls))

# sorted是高阶函数，可以接收一个key函数来实现自定义排序
print("数值绝对值排序", sorted(ls, key=abs))

print("字符串忽略大小写排序", sorted(strls, key=str.lower))
