
#searching a element in array-
#using in operator

lissst = [22,33,44,55,66,77,88]

if 22 in lissst:
    print(lissst.index(22))
else :
    print("the value doesnot exists")


#linearSearch
def linearSearch(list, value):
    for i in list:
        if i == value:
         return list.index(value)

print(linearSearch(lissst, 44))


#concatenate two  lists --> plus operator
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
list3 = list1 +list2
print(list3)

#concatenate two  lists --> * operator
list4 = [3]
print(list4*3)
max()
min()
sum()
