#find first and second best score, list may contains duplicates
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

def firstSecond(given_list):
    a = given_list  # make a copy

    a.sort(reverse=True)

    print(a)

    first = a[0]

    second = None

    for element in given_list:
        if element != first:
            second = element

            return first, second


print(firstSecond(myList))