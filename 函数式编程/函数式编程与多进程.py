import random


def gcd(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


def simplify(pair):
    n1, n2 = pair[0], pair[1]
    m = gcd(n1, n2)
    return (int(n1 / m), int(n2 / m))


data = [(random.randint(1, 1000), random.randint(1, 1000)) for _ in range(1000000)]


from multiprocessing import Pool  # 理论上这个就可以用，但是会卡住
#from multiprocessing.pool import ThreadPool as Pool
#from multiprocessing.dummy import Pool

p=Pool(4)

res4 = p.map(simplify, data)