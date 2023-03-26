#lists are ordered collection and mutable
list1 = [1,2,3,4,5]

print(1 in list1)  #true
print(7 in list1)  #false

#when access a element from last

print(list1[-0]) #1
print(list1[-1]) #1  when -1 is accessed it starts from last position

#use ----> for i in listOfStrings -->this is for string related lists

#use  ---> for i in range(0, len of list) -->this is when traversign a list of integers
shoppingList = ["w", "e", "r", "t"]
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "ssss"
    print(shoppingList[i])
print(shoppingList)

#insertion using three methods

#insert  ---> shoppingList.insert(0, "Ssss") insets at any index  , causes performance probllemin mehtod
#append  --> shoppingList.append("jjjk") this will add in the end of the list
#extend  --> add a list in the end

#slicing of lists

print(shoppingList[0:3])
print(shoppingList[:])


#deleting by three ways-->
#pop() --> delete last method in list,  time complexity O(1)/O(N)
#print(shoppingList.pop(2)) --> this will print the popped element from list
#delete()
del shoppingList[2]  #delete element at index 2  time complexity - O(N)
del shoppingList[1:3] #this will delete the 2 and 3 element

#remove()  --useful when we know the value itself, no need to provide the index here O(N)








