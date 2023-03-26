import itertools
import re
#
# str1 = "match a single character not present in the list below"
#
# pattern = r"(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])"
# output = re.findall(pattern, str1)
#
# print('\n'.join(output))

a_list = "1222311"


from itertools import groupby

for k,g in groupby(a_list):
    print((len(list(g)), int(k)), end = " ")