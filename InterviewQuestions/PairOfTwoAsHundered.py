#when two numbers sum is equal to target
list2 = [1, 2, 3, 2, 3, 4, 5, 6]
pair = []
def pairOfTwoAsHundered(list1, target):
    for i in range(0,len(list1)):
        for j in range(i+1, len(list1)):
            if list1[i]+list1[j] == target and list1[i] != list1[j]:
                print(list1[i], list1[j])
                print(i,j)

pairOfTwoAsHundered(list2, 6)





