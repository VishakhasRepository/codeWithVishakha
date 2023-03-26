num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def greator(n):
    return n > 5  # this will return boolean

res = list(filter(greator, num))
print(res)


from functools import reduce

lis1 = [1,2,3,4]
res = reduce(lambda x,y : x*y, lis1)
print(res)


