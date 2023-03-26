lis = ["cena", "randy", "ortan", "khali", "jindal"]

for item in lis:
    print(item, "and", end=" ")

# another way of writing the above programme is

print(" and ".join(lis))

# join function works upto length-1 times in order to join all the elements of the list
print("-".join(["Vishakha", "Saini"]))
