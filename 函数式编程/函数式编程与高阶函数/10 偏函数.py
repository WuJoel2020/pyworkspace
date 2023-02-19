print(int("101010", base=2))

from functools import partial

new_int = partial(int, base=2)
print(new_int("1010"))
print(new_int("101010"))
