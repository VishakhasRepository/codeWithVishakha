from itertools import permutations

input1, input2 = map(str, input().split(" "))
#input1, input2 = [str(x) for x in input().split(" ")]
print(input1)
print(input2)

permoutput = list(permutations(input1, int(input2)))
permoutput.sort()

for i in permoutput:
    print("".join(i))   #this is converting into String
    #print(i)



