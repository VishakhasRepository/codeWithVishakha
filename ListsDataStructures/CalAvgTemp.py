
noOfDays = int(input("How many days?"))
sum = 0
days = []
for i in range(1, noOfDays+1):
    temp = int(input("Day " + str(i) + "'s temp"))
    days.append(temp)
    sum = sum + temp
avg = round(sum/noOfDays, 2)  #rounded by 2 after
print(avg)
above = 0
for j in days:
    if j > avg:
        above +=1
print(str(above) + "days are above average temp")  #how many days above avg temperature


