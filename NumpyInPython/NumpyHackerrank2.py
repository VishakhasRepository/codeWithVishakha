import numpy

m1 = int(input())

n1 = []
n2 = []
for i in range(0,m1):
    m2 = list(map(int, input().split()))
    n1.append(m2)

for i in range(0,m1):
    m3 = list(map(int, input().split()))
    n2.append(m3)

#print(n1)
#print(n2)
arraym2 = numpy.array(n1)
arraym3 = numpy.array(n2)
#print(arraym2)
#print(arraym3)

print(numpy.dot(arraym2,arraym3))