import numpy

m1 = list(map(int, input().split()))
m2 = []
m3 = []

for i in range(0, m1[0]):
    m2.append(list(map(int, input().split())))
#print(m2)

for i in range(0, m1[1]):
    m3.append(list(map(int, input().split())))
#print(m3)


array_1 = numpy.array(m2)
array_2 = numpy.array(m3)

print(numpy.concatenate((array_1,array_2)))