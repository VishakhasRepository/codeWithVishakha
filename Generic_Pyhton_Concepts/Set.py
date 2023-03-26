s = set()
print(type(s))

s_from_list = set([1,2,3,4])
print(s_from_list)
print(type(s_from_list))
s_from_list.add(45)
print(s_from_list)  #set takes only unique values
s_from_list.add(45)
print(s_from_list)   #this will not add duplicate

#how to create new set
s2 = s_from_list.union({5,6,7})
print(s2)
s3 = s_from_list.intersection(1,4,6,7)
print(s3, s2)

#Start from 14 playlists