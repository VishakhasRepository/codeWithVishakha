
#very important, please do revise it
#sorting in ascending order
list = [12, 3, 56, 7, 2, 1, 9, 8]
for i in range(0, len(list)):
    for j in range(0, i+1):
        #print(list[i])
        #print(list[j])
        if list[i] < list[j]:
            list[i], list[j] = list[j], list[i]
print(list)



#arrange second lowest marks in albhabetically order
fullList = [["Aishakha", 55], ["Aishi", 44], ["Mishu", 55]]
secondSmallestNumber = [55,55]
albhabeticallyArrangedList = []
for i in fullList:
    if secondSmallestNumber[0] in i:
        albhabeticallyArrangedList = [i] + albhabeticallyArrangedList
print(albhabeticallyArrangedList)
albhabeticallyArrangedList.sort()
print(albhabeticallyArrangedList)
