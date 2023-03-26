from itertools import product

#the below one is very imp concept, it inludes list comphensions, lambda, map

# K, M = list(map(int, input().split()))   #3 1000
# list1 = []
# for i in range(K):
#     n2 = list(map(int, input().split()))[1:]
#     print(n2)
#     list1.append(map(lambda x:x**2%M, n2))
#
# print(max(map(lambda x:sum(x)%M, product(*list1))))
#https://www.hackerrank.com/challenges/input/problem?isFullScreen=true

k, m = list(map(str, input().split()))
int1 = input().replace("x", k)
#print(eval(int1))
if eval(int1) == int(m):
    print(True)










