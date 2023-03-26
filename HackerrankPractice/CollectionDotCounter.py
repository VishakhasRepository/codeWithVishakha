# Enter your code here. Read input from STDIN. Print output to STDOUT
#10 --> no. of shoes
#2 3 4 5 6 8 7 6 5 18 -->list of all shoe sizes, 6 size avalaible 2 quantity, 5 #also 2 quantity
#6 --> No. of customers
# 6 is the size and 55 is the price


#A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

from collections import Counter

TotalShoes = input()
ListOfAllSizes = str(input())
NoOfCustomers = int(input())
list2 = ListOfAllSizes.split(" ")
dict1 = Counter(list2)

def functionMain():
    priceAdd = 0
    for i in range(1, NoOfCustomers + 1):

        SizeAndPrice = input().split(" ")
        SizeOfShoe = int(SizeAndPrice[0])
        SizeOfShoeString = SizeAndPrice[0]
        PriceOfShoe = int(SizeAndPrice[1])
        if SizeOfShoeString in dict1.keys():
            if dict1[SizeOfShoeString] != 0:
                priceAdd += PriceOfShoe
                dict1[SizeOfShoeString] = dict1[SizeOfShoeString] - 1

    return priceAdd

print(functionMain())



#converting two lists in as key value in dictionary
#res = dict(zip(sizeList, priceList)) #cannot use dictionary because it does not take duplicate key






