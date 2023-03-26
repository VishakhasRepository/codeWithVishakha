
"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
title()---->this capitalize the first albhabet in the string
"""
import string

s = "vishakha saini"
#s = "12abc"
str = s.split()
for i in range(len(str)):
    str[i] = string.capwords(str[i])

print(str)
print(' '.join(str))

#The below one worked for the hackerrank problem
s = "a12abcd asasas"
splitted_string = s[:].split()
print(splitted_string)
for x in splitted_string :
    print(x)
    s = s.replace(x, x.capitalize()) #in this the words are replaced with capital first letter word
print(s)



