#both the list has same content or no?

list1 = ["z", "i", "c"]
list2 = ["i", "z", "c"]

def permutationOfAlist(list1, list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        print("yes")
    print("no")

permutationOfAlist(list1, list2)



