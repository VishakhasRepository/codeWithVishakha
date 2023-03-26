# String formatting means insert a variable in string

# I st method

import math

m = "Hello"
print("This is insane %s Hi" % m)

# 2nd tarika
me = "Vishakha"
a1 = 3
print("Hey How are you %s %s" % (me, a1))   #we have passed atuple, but this is not readeable

#3rd tarika using format
me = "Vishakha"
a1 = 3
a = "This is {} {}"
print(a.format(me, a1))

a = "This is {1} {0}"
print(a.format(me, a1))

#another way of doing using F strings  ---->most preferred way in python
a = f"This is {me} {a1} {4*65} {math.cos(65)}"  #can use pyhton variable expression also, we have used f to make i as f strings f means fast
print(a)
