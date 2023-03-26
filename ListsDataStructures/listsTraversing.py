

list1 = [1,2,3,4,5,6,7]

def findAverageOfNumber():
    value = 0
    mylist = []
    while(True):
        int1 = input("Please type integer")
        if int1 == "done" : break
        value = float(int1)
        mylist.append(value)
        avarage = sum(mylist)/len(mylist)
    print(avarage)

#findAverageOfNumber()

#create lists from string
list2 =[]
str = "ssssss"
for i in str:
    list2.append(i)
print(list2)

print(list(str))  #using list function

#using split to split a sting into list
str2 = "rrt-rre-yyu"
print(str2.split("-"))

#convert list to string back
list4 = ["ee", "rr"]
deli = 'u'
print(deli.join(list4))

#difference between list1.sort() and sorted(list1) method in python
#sort will modify the original list but sorted will nort


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[::2] = 10, 20, 30, 40, 50, 60
print(a)

