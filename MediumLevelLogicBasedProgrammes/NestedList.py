"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
5
Harsh
20
Beria
20
Varun
19
Kakunami
19
Vikas
21

fullList = [["Harsh", 20], ["Beria", 20], ["Varun", 19], ["Kakunami", 19], ["Vikas", 21]]
"""

list1 = []
allmarkslist = []

fullList = [["Harsh", 20], ["Beria", 20], ["Varun", 19], ["Kakunami", 19], ["Vikas", 21]]

for j in list1:
    allmarkslist = [j[1]] + allmarkslist

allmarkslist.sort()
total_count_of_smallest_number = allmarkslist.count(allmarkslist[0])
min_val = allmarkslist[total_count_of_smallest_number]
for i in range(total_count_of_smallest_number, len(allmarkslist)):
    if min_val >= allmarkslist[i]:
        list2 = [allmarkslist[i]] + list2

albhabeticallyArrangedList = []
for i in list1:
    if list2[0] in i:
        albhabeticallyArrangedList = [i] + albhabeticallyArrangedList
albhabeticallyArrangedList.sort()

for i in albhabeticallyArrangedList:
    print(i[0])
