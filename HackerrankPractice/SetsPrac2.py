# sizeM = int(input())
# setM = {map(int, input().split())}
# sizeN = int(input())
# setN = {map(int, input().split())}

sizeM = 4
setM = {2, 4, 5, 9}
sizeN = 4
setN = {2,4,11,12}

set1 = set()
#print(setM.difference(setN))
#print(setN.difference(setM))
set1.update(setM.difference(setN))
set1.update(setN.difference(setM))
set2 = sorted(set1)  #to arrange in asccending order
for i in set2:
    print(i)