import functools as func
print(sum([func.reduce(lambda x, y: x*y, map(int, input().split('0 '))) for i in range(3)]))
