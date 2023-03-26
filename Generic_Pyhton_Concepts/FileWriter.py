#f = open("Vishakha.txt", "w")  #this mode is to overwrite the file so use a for appending the content in the file
#f.write("Hello") #This will overwrite the content in the file


f = open("Vishakha.txt", "a")
uio = f.write("Hello\n")
print(uio)   #this returns the number of characters appended in the file
f.close()

#Handle read and write both
f = open("Vishakha.txt", "r+")
f.read()
f.write("Thank You")
f.close()