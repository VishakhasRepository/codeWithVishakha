# dictionary is key value pairs
dict1 = {}
print(type(dict1))

dict2 = {"Vishakha": "Burger", "ABC": "Roti", "DEF": "Rice",
         "AnjanVyakti": {"Morning": "Daliya", "Afternoon": "Poha", "Night": "Milk"}}
print(dict2)
print(dict2.keys())
print(dict2["AnjanVyakti"]["Morning"])
# keys should be immutable


# how to add more items in dictionary
dict2["Bhaisahab"] = "Junk Food"
dict2["Auranjeb"] = "Kebabs"
print(dict2)

del dict2["Bhaisahab"]
print(dict2)
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print(dict2.copy())

d3 = dict2   #here d3 has all the values of dict2 but when we change anything in d3, it affects dict2 because d3 is only pointer to dict2
print(d3)

del d3["Auranjeb"]
print(dict2)

d3 = dict2.copy()  #here d3 is copy of dict2 but not poiting to dict2 hence change in d3 will not affect d3
del d3["Vishakha"]  #this change has only affected d3
del dict2["DEF"]  #this change has not affected d3
print("..................................................................................................................................................")
print(dict2)
print(d3)



#Some more functions
print(dict2.get("Vishakha"))
print(dict2.update({"Vishakha":"Burger2"})) #it got updated, same as line no. 15 and 14
print(dict2)
print("itemsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
print(dict2.items())
print(dict2.values())

