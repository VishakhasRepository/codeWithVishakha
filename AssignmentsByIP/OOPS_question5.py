# Q5. Create an empty dictionary called Car_0 . Then fill the dictionary with Keys : color , speed
# , X_position and Y_position.
# car_0 = {'x_position': 10, 'y_position': 72, 'speed': 'medium'} .
# a) If the speed is slow the coordinates of the X_pos get incremented by 2.
# b) If the speed is Medium the coordinates of the X_pos gets incremented by 9
# c) Now if the speed is Fast the coordinates of the X_pos gets incremented by 22.
# Print the modified dictionary.

# Car_0 = {}
Car_0 = {'X_position': 10, 'Y_position': 72, 'speed': 'fast'}

# for i in range(0,3):
# Car_0[input()] = input()  #taking input from user both for key and value

def findPosition():
    for k, v in Car_0.items():
        if v == "medium":
            Car_0["X_position"] = Car_0["X_position"] + 9
            return Car_0

        elif v == "slow":
            Car_0["X_position"] =  Car_0["X_position"] + 2
            return Car_0

        elif v == "fast":
            Car_0["X_position"] = Car_0["X_position"] + 22
            return Car_0

print(findPosition())
