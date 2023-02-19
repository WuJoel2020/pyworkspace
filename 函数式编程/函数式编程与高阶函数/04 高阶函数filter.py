# 在一个列表中，删掉偶数，保留奇数
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 7])))


# 删除序列中的空字符串
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ["A", "", "B", None, "C", "  "])))
