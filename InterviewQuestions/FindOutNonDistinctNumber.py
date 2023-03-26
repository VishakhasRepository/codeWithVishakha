
list1 = [1,2,3,4,5,6,6,7,8,8]

def findNonDistinctOne(list1):
    for i in range(0, len(list1)):
        for j in range(i+1, len(list1)):
            if list1[i] == list1[j]:
                print(list1[i])

findNonDistinctOne(list1)








