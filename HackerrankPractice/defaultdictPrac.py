

#just an example
#list4 = [1,2,3,4,5,6]
#print(" ".join(map(str, list4)))

from collections import defaultdict
d = defaultdict(list)
list1=[]

n, m = map(int,input().split())    #taking one input and splitting it in two parts
print(n)  #5
print(m)  #2

for i in range(0,n):
    d[input()].append(i+1)
print(d)

for i in range(0,m):
    list1=list1+[input()]
print(list1) #a, b

for i in list1:
    if i in d:
        print(" ".join(map(str,d[i])))
    else:
        print(-1)