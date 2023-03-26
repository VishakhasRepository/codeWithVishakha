# setM = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 52}
#
# func1 = ["intersection_update", "10"]
# setN = {2, 3, 5, 6, 8, 9, 1, 4, 7, 11}
#
# func2 = ["update", "2"]
# setB = {55, 66}
#
# func3 = ["symmetric_difference_update", "5"]
# setc = {22, 7, 35, 62, 58}
#
# func4 = ["difference_update", "7"]
# setd = {11, 22, 35, 55, 58, 62, 66}
#
# setM.intersection_update(setN)
# print(setM)
# setM.update(setB)
# print(setM)
# setM.symmetric_difference_update(setc)
# print(setM)
# setM.difference_update(setd)
# print(sum(setM))

a = input()
setM = set(map(int, input().split()))
b = int(input())
for i in range(0,b):
    #newSet = set()
    funcName = input().split()
    newSet = set(map(int,input().split()))
    if funcName[0] == "intersection_update":
        setM.intersection_update(newSet)
    elif funcName[0] == "update":
        setM.update(newSet)
    elif funcName[0] == "symmetric_difference_update":
        setM.symmetric_difference_update(newSet)
    elif funcName[0] == "difference_update":
        setM.difference_update(newSet)


print(sum(setM))
