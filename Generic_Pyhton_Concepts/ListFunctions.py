list1 = ["aaloo", "bhindi", 23, "gajar"]
numbers = [1, 2, 3, 4, 33, 6, 7, 8]

numbers.sort()  # this changes original list
print(numbers)
# numbers.reverse()  #this changes original list
# print(numbers)

for a in list1:
    print(a)

print(numbers[1:2:-1])
print(numbers[:])  # default values
print(numbers[1:4])
print(numbers[1:2])  # slicing returns list
print(numbers[1:2:1])
print(numbers[1:2])
numbers.append(22)  # adds in the end
print(numbers)
numbers.insert(3, 34)
print(numbers)
numbers.remove(34)
print(numbers)
numbers.pop()  # removes from end
print(numbers)

# list is mutable but tuple is immutable

tup1 = (1, 2, 3, 4, 5)
tup1.insert(2, 33)  #tuple cannot be modified
