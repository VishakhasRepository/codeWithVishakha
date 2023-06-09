
# Q-10. What will be the output of the following code snippet?  important concept

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1   #['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list3 = fruit_list1[:]   #['Apple', 'Berry', 'Cherry', 'Papaya']
print(fruit_list1)
print(fruit_list2)
print(fruit_list3)

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

print(fruit_list2)  #['Guava', 'Berry', 'Cherry', 'Papaya']
print(fruit_list3)  #['Apple', 'Kiwi', 'Cherry', 'Papaya']
print(fruit_list1)  #['Guava', 'Berry', 'Cherry', 'Papaya']  this list will get modifies if list2 is modified becauselist 1 is assigned to lis2

print(fruit_list1, fruit_list2, fruit_list3)


sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    print(ls)
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print(sum)
# A. 22
# B. 21
# C. 0
# D. 43