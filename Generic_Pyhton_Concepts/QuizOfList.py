list1 = [34, 2, "we", "rt", "gh", 3, 4, 7, 8, 9, 77]

for item in list1:
    if type(item) == int and item >6:
        print("This is integer-- " + str(item))

        #can use isNumeric() also
