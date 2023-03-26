


import re

x,y = input(), input()
pattern = re.compile(y)
print(y)
r = pattern.search(x)   #0,2
print(r)
if not r :print("(-1,-1)")
while r:
    print((r.start(),r.end()-1))
    r = pattern.search(x,r.start() + 1)


