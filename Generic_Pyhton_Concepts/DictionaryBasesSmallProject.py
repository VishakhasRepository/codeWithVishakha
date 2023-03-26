userInput = input("Which word meaning you want to know?")
print(userInput)

dictMine = {"Red": "RedColor", "Yellow": "YellowColor"}
print(dictMine.get(userInput))
# one more way
print("the meaning of the word is: " + dictMine[userInput])
