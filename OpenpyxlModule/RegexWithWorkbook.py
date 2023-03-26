import openpyxl

workbook = openpyxl.load_workbook("Employees.xlsx")
#print(workbook.sheetnames)

sheetData = workbook["EmployeeData"]

#print(sheetData.dimensions)
#for row in sheetData.values:
   # print(row)   #print all values in the form of tuple

data = []
for row in sheetData.values:
    a,b,c,d,e,f,g = row
    data.append("{};{};{};{};{};{};{}".format(a,b,c,d,e,f,g))

#now join the elements of the list using new line delimeter
employees = "\n".join(data)


import re

#scenario= match the last name of all the employees whose salary is less than 30 k but atleast 24 k dollars means between 24000 - 29999
#  20;Adrian;Harrison;IT;1234567909;20th Address, LA;21160
regex_applied_data = re.findall(r"\d{1,};.+?;(.+?);.+;[2][4-9]\d{3}", employees)


#match all employyes last names and department from it or marketing department and whose last naes are not m0re that 5 characters long
regex_applied_data = re.findall(r"\d{1,};.+?;(\w{1,5});(IT|Marketing);.+;\d{5}", employees)


#what is we dont want to include the departmrnt names in the result so for this we will be using the non capturing groups
regex_applied_data = re.findall(r"\d{1,};.+?;(\w{1,5});(?:IT|Marketing);.+;\d{5}", employees)


#match all employees first name start with letter P or subsequent(start with any letter after P and with P) letter in english alphabet and phone number of those employees should start with even digits 24 6 8 and ends with an odd digit 13579
regex_applied_data = re.findall(r"\d{1,};([P-Z].+?);.+?;.+?;[2468]\d+[13579];.+", employees)

#match first and last name as well phone nmber --> who are located in new york and are working in sales department
regex_applied_data = re.findall(r"\d{1,};(.+?);(.+?);Sales;(.+?);.+New York;.+?", employees)


results = [" ".join(i) for i in regex_applied_data]
#print(results)

#Negative look ahead assertion(match somehting as long as it is not followed by a certain pattern), find match the lname name as long as their address does not at Miami
regex_applied_data = re.findall(r"\d{1,};.+?;(.+?);.+?;.+(?!Miami);.+?", employees)

print(regex_applied_data)