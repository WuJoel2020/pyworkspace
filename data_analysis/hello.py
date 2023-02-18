import sys
if len(sys.argv) > 1:
    x = sys.argv[1]
else:
    x = 0
hello = 'hello world' + str(x)
print(hello)