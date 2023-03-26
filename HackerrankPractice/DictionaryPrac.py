
NoOfCustomers = 6
dict1 = {'5': 2, '6': 2, '2': 1, '3': 1, '4': 1, '8': 1, '7': 1, '18': 1}
#sizeList = ['6', '6', '6', '4', '18', '10']
#priceList = ['55', '45', '55', '40', '60', '50']


priceAdd = 0
for i in range(1, NoOfCustomers+1):
    #print(i)

    SizeAndPrice = input("SizeAndPrice").split(" ")
    SizeOfShoe = int(SizeAndPrice[0])
    SizeOfShoeString = SizeAndPrice[0]
    PriceOfShoe = int(SizeAndPrice[1])
    if SizeOfShoeString in dict1.keys():
        #print(dict1[SizeOfShoeString])
        if dict1[SizeOfShoeString] != 0:
            priceAdd += PriceOfShoe
            dict1[SizeOfShoeString] = dict1[SizeOfShoeString] - 1
print(priceAdd)  #250



