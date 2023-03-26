import random

random_number = random.randint(2,8)
print(random_number)

random_number2 = random.random()*100  # this generates random number between 1 to 100
print(random_number2)

lst = ["starplus", "dd1", "aajtak"]
choice = random.choice(lst)
print(choice)   #this is giving random value


#how to install module---->  type pip sklearn in terminal