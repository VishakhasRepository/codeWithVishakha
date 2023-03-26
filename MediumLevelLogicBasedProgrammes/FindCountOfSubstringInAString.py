
# string1 = "abcdefghiijkghilmnghibvcghi"   #find count of ghi
# substring = "ghi"
#
# if "ghi" in string1:
#     print(string1.count("ghi"))


#what is a string is like this - ABCDCDC
#string-count-with-overlapping-occurrences

string = "ABCDCDC"
sub_string = "CDC"

count = 0
for i in range(len(string)):
    if string[i:len(sub_string)+i] == sub_string:  #this is comparing like ABC with CDC then BCD with CDC then CDC with CDC then DCD with CDC .....
        count += 1
print(count)