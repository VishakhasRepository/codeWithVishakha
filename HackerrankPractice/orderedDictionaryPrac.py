
#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

import re
from collections import OrderedDict

# in1 = int(input())
# dict1 = OrderedDict()
# for i in range(in1):
#     totalLenWord = input()
#     key1 = totalLenWord[:-2].strip()
#     value1 = int(totalLenWord[-2:])
#     print(dict1.get(key1, 0))   #this returns th value of the key and if it is not present then this will return 0, this whole gives value
#     dict1[key1] = dict1.get(key1, 0) + value1
#     print(str(key1) + " "+ str(dict1[key1]))
#
# print(dict1)

in1 = int(input())
dict1 = OrderedDict()
for i in range(in1):
    totalLenWord = input()
    value1 = re.findall('[0-9]', totalLenWord)
    value2 = ''.join(value1)
    key1 = re.findall('[^\d]', totalLenWord)
    key2 = (''.join(key1)).strip()
    dict1[key2] = dict1.get(key2, 0) + int(value2)
for i in dict1:
    print(i, dict1[i])
