import itertools
from itertools import product

a = list(map(int, input().split()))  #converting map object into list
print(a)  # [1, 2]
b = list(map(int, input().split()))

print(*product(a, b))   #(1, 3) (1, 4) (2, 3) (2, 4)


#using list comphrensions
A = [int(x) for x in input().split()]  #alrea inside bracket so returning list
print(A)  # [1, 2]
B = [int(y) for y in input().split()]

print(*itertools.product(A, B))   #(1, 3) (1, 4) (2, 3) (2, 4)


#without list

a = map(int, input().split())
print(a)   #<map object at 0x0000021174F64F70>
b = map(int, input().split())

print(*product(a, b))   #(1, 3) (1, 4) (2, 3) (2, 4)