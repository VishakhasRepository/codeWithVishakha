"""
File IO Basics

r - open file for reading, default mode
w - Open a file for writing
x - Creates file if not exists
a - Add more content to a file, append
t - text mode(opens file in text mode), default mode
b - binary mode
+ - read and write mode
"""

f = open("Vishakha.txt", "rt")  # this opens the file, return file pointer, rt mode is default mode read and text
content = f.read(3)  # once content is read then this will not read the content again
print("1- ", content)

# content = f.read()
# print("0- ", content)

# content = f.read()
# print("2- ", content)  #it is printed blank


for line in content:
    print(line)  # this is printing character by character

for line in f:
    print(line, end="")  # this is printing line by line, after using new line character in "end" print statement is not giving extra line in the results

f.close()  # if a file is opened then it should be closed too

# print by default gives backslash n character \n
