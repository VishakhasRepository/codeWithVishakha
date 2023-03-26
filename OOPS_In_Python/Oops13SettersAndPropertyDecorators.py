class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} and {self.lname}"

    def printemail(self):
        return f"{self.fname}.{self.lname}@gmail.com"

hindustani_supporter = Employee("Hindustani", "Supporter")   #object creation k time pe constructor call hota hai
Vishakha_lol_Saini = Employee("Vishakha", "Saini")

print(hindustani_supporter.explain())
#print(hindustani_supporter.email)  #Hindustani.Supporter@gmail.com
print(hindustani_supporter.printemail())

#now i will change first name
hindustani_supporter.fname = "US"
print(hindustani_supporter.explain())  #This employee is US and Supporter

#print(hindustani_supporter.email)   #it is still printing this - Hindustani.Supporter@gmail.com. it has not changed the fname to us
#run time pe object create hua and set krdiya
#this is because since while creating objects fname and lname was initialized as hindustani supporter hence after calling expalin method, the same is appearing
#so to avoid this thing we use setters

print(hindustani_supporter.printemail())




