lis1 = ["Bhindi", "chopstics", "Aloo", "chowmein"]

i = 1
for item in lis1:
    if i%2 is not 0:
        print(f"Jarvis please buy {item}")
    i = i + 1

# so in above method we had to use i variable as extra, better appraoch is to use enumerate function

for i, item in enumerate(lis1):
    if i%2 is 0:        #here index starts from 0, upwards we started from 1
        print(f"Jarvis please buy {item}")


#If you dont want to this below line to get printed when this file is imported than use this if condition
if __name__ == '__main__':
    print("Hello I am Vishakha")
