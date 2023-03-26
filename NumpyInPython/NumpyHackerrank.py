import numpy

# m1 = list(map(int, input().split()))
# # m2 = list(map(int,input().split()))
# # m3 = list(map(int,input().split()))
# m4 = []
# for i in range(0, m1[0]):
#     m4.append(list(map(int, input().split())))
#
#
# my_array = numpy.array(m4)
# print(numpy.transpose(my_array))
# print(my_array.flatten())
#print(numpy.prod(numpy.sum(my_array, axis = 0)))
#print(numpy.prod(my_array, axis=None))


m1 = list(map(int, input().split()))

n1 = []
n2 = []
for i in range(0,m1[0]):
    m2 = list(map(int, input().split()))
    n1.append(m2)

for i in range(0,m1[0]):
    m3 = list(map(int, input().split()))
    n2.append(m3)


print(n1)
print(n2)
arraym2 = numpy.array(n1)
arraym3 = numpy.array(n2)
print(arraym2)
print(arraym3)
print(numpy.add(arraym2, arraym3))
print(numpy.subtract(arraym2, arraym3))
print(numpy.multiply(arraym2, arraym3))
print(numpy.floor_divide(arraym2, arraym3))
print(numpy.mod(arraym2,arraym3))
print(numpy.power(arraym2, arraym3))

