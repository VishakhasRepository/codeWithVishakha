def function1():
    print("Hello")


func = function1  # whenever we are assigning then dont use parenthesis for functions
func()
del function1  # after deleting a function, still the copy of the function is stored in func hence this will print hello
func()


def funcret(num):
    if num == 0:
        return print  # we can return a function using a function
    if num == 1:
        return sum  # we can return a function using a function


a = funcret(1)
print(a)  # this is printing a built in function


# how to provide a function as a argument
def executor1(funcPass):
    funcPass("Hello Vishakha")


executor1(print)  # passed a print function inside the brackets

def dec1(func1):  #this takes func as a argument
    def nowexec():
        print("Executing now")  #this can be used to connect with server or db connection etc
        func1()
        print("Executed")
    return nowexec

@dec1    #like this we can use with @ too
def whoisvishi():
    print("vishakha is good girl")

#whoisvishi =  dec1(whoisvishi)  # instead of this line we can use a @dec1 on top of the function#

whoisvishi()
