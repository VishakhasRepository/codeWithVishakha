# Create a nested tuple from the dictionary, with each item in the tuple as a key value pair
# from the dictionary
from collections import defaultdict

test_dict = {'gfg' : {'x' : 5,
                      'y' : 6},
             'is' : {'x' : 1,
                     'y' : 4},
             'best' : {'x' : 8,
                       'y' : 3}}

res = defaultdict(tuple)
print(type(res))
for key, val in test_dict.items():
    for ele in val:
        print(ele)
        print(res[ele])
        print(val[ele])
        print("----------------")
        res[ele] = res[ele] + (val[ele], )
print(res.items())  #([('x', (5, 1, 8)), ('y', (6, 4, 3))])