
lis2 = [100,3,4,5,6,7,8,9,22,33]
def findMaxOfProductTwoNumberInList(lis1):
    maxProdcut = 0
    for i in range(0, len(lis1)):
        for j in range(i+1, len(lis1)):
            if lis1[i] * lis1[j] > maxProdcut:
                maxProdcut = lis1[i] * lis1[j]
    print(maxProdcut)

findMaxOfProductTwoNumberInList(lis2)


#remove first and last out of a list


def middle(lst):
    new = lst[1:]
    del new[-1]
    return new