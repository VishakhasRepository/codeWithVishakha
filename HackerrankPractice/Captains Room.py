
#K = int(input())
#list1 = map(int, input().split())


#n = int(input())


K = 5
list1 = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]

#list_room = list(map(int, input().split()))
#set_room = set(list1)
#print(set_room)
# print(int(sum(i*K for i in set_room)))
# #print(sum(list1)/(K-1))
# print(sum(list1))
# print(int((sum(i*K for i in set_room) - sum(list1))/(K-1)))
#
# dict1 = {}
# for i in list1:
#     if i in dict1:
#         dict1[i] = dict1[i] + 1
#     else:
#         dict1[i] = 1
#
# print(min(dict1.values()))
#
# value = [i for i in dict1 if dict1[i]==min(dict1.values())]
# #
# # for key, value in dict1.items():
# #     print(key, value)
#
# print(int(value[0]))

from collections import Counter

if __name__ == "__main__":
    _ = 5
    print(Counter(list1))
    print(Counter(list1).most_common())
    print(Counter(list1).most_common()[-1][0])

