# int_list = [2, 3, 6, 8, 9, 3]
#
#
# # using recursion, did not understand it
#
# def smallest(int_list):
#     if (len(int_list) == 1):
#        return int_list[0]
#     else:
#         a = smallest(int_list[1:])
#         b = int_list[0]
#
#         if (a <= b):
#             return a
#         else:
#             return b
#
#
# print(smallest(int_list))
#
# # this is the second method
#
# l1 = [12, 32, 4, 34, 64, 3, 43]
# for i in range(0, len(l1)):
#     for j in range(0, i + 1):
#         if l1[i] < l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
# min_val = l1[1]
# for k in l1:
#     if min_val > k:
#         break
# print(min_val)
#
#
# #using sort for above method
# l1.sort()
# min_val = l1[1]
# for k in l1:
#     if min_val > k:
#         print(f"min value is {min_val}")
#         break


#how to find all second smallest numbers, what if the smallest number is occurring two times

list1 = [2,3,3,4,5,6,7,3,3,3,3,3,3,5,2]
list2 = []
list1.sort()
#print(list1)
total_count_of_smallest_number = list1.count(list1[0])
#print(total_count_of_smallest_number)
min_val = list1[total_count_of_smallest_number]
print(min_val)

for i in range(total_count_of_smallest_number, len(list1)):
    if min_val >= list1[i]:
        list2 = [list1[i]] + list2    #here it is getting appended
print(list2)






