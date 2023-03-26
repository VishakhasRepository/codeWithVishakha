"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""

n = int(input("How many"))
student_marks = {}
for _ in range(n):
    name, *line = input("Write name and their marks").split()
    print(name)
    print(*line)  #these are the marks after split by space
    scores = list(map(float, line))   #all line variable value converting into list
    print(scores)
    student_marks[name] = scores   #it is a dictionary with values in the list, hence this is converting all the line variable values into the list

query_name = input("Which name you want to query - ")
print(student_marks[query_name].count(student_marks))
count = 0
for i in student_marks[query_name]:
    count = count+1
print(count)

print("{:.2f}".format(sum(student_marks[query_name])/count))   #this is printing till two decimal points
