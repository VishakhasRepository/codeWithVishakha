lq = 10 #Global Variable   can be accessed by a method

def function_1():
    l = 8
    m = 9
    print(l,m)
    global lq  #now lq can be changed in next line using global varaible
    lq = 10 + lq  #python does not give permission to change global variable directly, need to use global keyword
    print(lq)

function_1()
print(lq)  # a method variable called a local variable can be accesses outside a mehtod, to make it access outside a method Global keyword is required.


print("----------------------------------------------------------------------------------------------------------------------------------------------------")


#x = 89
def function_abc():
    x = 20
    def function_inner_abc():
        global x
        x = 88  #here global keyword is not assigning 33 to x because global variable searches outside both the functions always hence global will create another variable x outside the scope of methods
    print("before calling inner function", x)
    function_inner_abc()
    print("after calling inner function", x)

function_abc()
print(x) #This is that variable which is created outside the scope of the two methods