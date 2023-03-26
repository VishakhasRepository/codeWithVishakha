"""Use while loop
how many time you and computer won, display it on the screen
number of chances is 10 for both, 5 each
take input from user(computer)
choose one from s w g and store it in variable
gun kills snake and gun wins, snake drinks water and snake wins, gun gets submerged in water and water wins
use random.choice function, using this function choice any of three but don't get it print it will remain inside program.
"""
import random

chances = 10
vishakha__points = 0
computer__points = 0

while chances > 0:
    list1 = ["s", "w", "g"]
    print(f"This is your {chances} chance")
    computer_choice = random.choice(list1)
    print(f"Computer choice is {computer_choice}")
    vishakha_choice = input("Enter your choice among s, w, g")

    if vishakha_choice == computer_choice:
        print("Both has same choice")
        vishakha__points = vishakha__points + 0
        computer__points = computer__points + 0

    elif vishakha_choice == "s":
        if computer_choice == "w":
            print("Vishakha wins")
            vishakha__points = vishakha__points + 1
        elif computer_choice == "g":
            print("computer wins")
            computer__points = computer__points + 1

    elif vishakha_choice == "w":
        if computer_choice == "s":
            print("computer wins")
            computer__points = computer__points + 1
        elif computer_choice == "g":
            print("vishakha wins")
            vishakha__points = vishakha__points + 1

    elif vishakha_choice == "g":
        if computer_choice == "w":
            print("computer wins")
            computer__points = computer__points + 1
        elif computer_choice == "s":
            print("vishakha wins")
            vishakha__points = vishakha__points + 1

    chances = chances - 1
print(f"The total points of Vishakha are - {vishakha__points}")
print(f"The total points of computer are - {computer__points}")
