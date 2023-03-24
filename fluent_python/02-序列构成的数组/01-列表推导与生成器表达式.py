colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]  # 列表推导式
print(tshirts)

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):  # 生成器表达式
    print(tshirt)

for tshirt in [(c, s) for c in colors for s in sizes]:  # 列表推导式
    print(tshirt)
