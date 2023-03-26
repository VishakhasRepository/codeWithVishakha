# no. of guesses 9
# print no. of guesses left
# No. of guesses he took to finish
# game over

print("Total number of guess are 9")
guesses = 9
total = 0
while guesses > 0:
    print("The number of guesses left - " + str(guesses))

    num1 = int(input("Enter the guessed number between 21 and 30\n"))
    ans = 22
    total = total+1
    if num1 == ans:
        print("You guessed correct number")
        print("The total number of attempts are - " + str(total))
        break

    elif num1 > ans:
        print("Your guessed number is greater than the actual one")

    elif guesses == 1:
        print("GAME OVER - out of chances")
        break
    else:
        print("Your guessed number is smaller than the actual one")

    guesses = guesses - 1
