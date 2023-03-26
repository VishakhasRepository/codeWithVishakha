str1 = "i am a Good girl"
print(str1[0:4])
print(str1[0:10:2])
print(str1[:4:])
print(str1[::])
print(len(str1))
print(str1[-4:-2])
print(str1[::-1])  #reverted the string
print(str1.isalnum())   #false since this is not a alphanumeric string, since it has spaces
print(str1.isalpha()) #alphabets, has spaces
print(str1.endswith("girl"))
print(str1.count("o"))
print(str1.capitalize())
print(str1.find("am"))
print(str1.lower())
print(str1.upper())
print(str1.replace("am", "are"))
