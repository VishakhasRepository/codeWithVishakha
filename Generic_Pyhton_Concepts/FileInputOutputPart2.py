f = open("Vishakha.txt", "rt")
#print(f.readline())  #this reads one line at a time
#print(f.readline())
#print(f.readlines())  #this stores line into list --->['Vishakha is good girl\n', 'Vishakha is very smart\n', 'She is beauty with brains']

print(f.readline())
print(f.tell())   #this tells where is file pointer
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)  #This resets the pointer
print(f.readline())


