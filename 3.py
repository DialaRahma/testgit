x31 = [i for i in range(0, 50)]


def slice(x):
    return x[0], x[1:]


def ops(x):
    return x[0]+x[-1], x[0]-x[-1], x[0]*x[-1], x[0] % x[-1]


def sumallNb(x):
    return sum(x)


def oddNbIndex(x):
    return x[1::2]


def copyList(x):
    return x[-1:0:-1]


def limitList(x):
    return x[-1::-1]


def limitList(x):
    return [1 if el % 2 == 0 else 0 for el in x]


print(slice(x31))
print(ops(x31))
print(sumallNb(x31))
print(oddNbIndex(x31))
print(copyList(x31))
print(limitList(x31))
