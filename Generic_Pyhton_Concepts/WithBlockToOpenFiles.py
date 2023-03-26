with open("Vishakha.txt") as f:     #using this not required to close files
    a = f.readlines()
    print(a)


#Would it read again? yes since in with block file is read and it is closed also so when you read again it will get read.
f = open("Vishakha.txt")
content = f.read()
print(content)
