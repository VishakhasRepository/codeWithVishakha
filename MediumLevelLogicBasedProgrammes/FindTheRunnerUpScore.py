"""
Find the Runner-Up Score

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

"""
from functools import reduce

participants_list_scores = [1, -1, -2 ,-1]   #ans should be 7

participants_list_scores.sort(reverse= True)
print(participants_list_scores)


count_of_first_index_value = participants_list_scores.count(participants_list_scores[0])
print(participants_list_scores[0])
print(count_of_first_index_value)


print(f"The runner score is {participants_list_scores[count_of_first_index_value]}")

#Another possible way of doing it, the below one is also a nice logic

lis = [1, 1, -1, -2 ,-1]
z = max(lis)
while max(lis) == z:     #this logic works on double highest score too
    lis.remove(max(lis))

print(f"The max list is {max(lis)}")


#the below logic is to find the greatest number from the list
nums = [1, 1, -1, -2 ,-1]
print(reduce(lambda x,y: x if x>y else y, nums))



#the below code is working
nums = [1, -1]
myList = sorted(set(map(int, nums)))  #set takes unique values
print(myList)
print(myList[len(myList)-2])   #did not understand 2 logic here


